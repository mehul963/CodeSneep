from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.urls import reverse_lazy

import shlex
import subprocess
from importlib.machinery import SourceFileLoader

from quiz.models import Question, Choice, QuizAttempt, ProgramingQuestion, Submission
from quiz.forms import UserCreationForm
import os

class SignUpView(TemplateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def get(self, request):
        return self.render_to_response({})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("quiz")

        return redirect("signup")


class QuizView(LoginRequiredMixin, TemplateView):
    template_name = "quiz.html"

    def get_login_url(self) -> str:
        return reverse_lazy("login")

    def get(self, request):
        quizattempts = QuizAttempt.objects.filter(user=self.request.user)
        if any(list(quizattempts.values_list("is_submitted"))):
            return redirect("programing_question")
        if not quizattempts:
            easy_questions = Question.objects.filter(difficulty="EASY").order_by("?")[
                :5
            ]

            medium_questions = Question.objects.filter(difficulty="MEDIUM").order_by(
                "?"
            )[:3]

            hard_questions = Question.objects.filter(difficulty="HARD").order_by("?")[
                :7
            ]

            attempts = [
                QuizAttempt(user=self.request.user, question=question)
                for question in [*medium_questions, *easy_questions, *hard_questions]
            ]
            quizattempts = QuizAttempt.objects.bulk_create(attempts)

        context = {"quizattempts": quizattempts}
        return self.render_to_response(context=context)

    def post(self, request):
        score = 0
        user = request.user
        quizattempts = QuizAttempt.objects.filter(user=user)

        for quizattempt in quizattempts:
            question = quizattempt.question
            choice_id = request.POST.get(f"question:{question.pk}")
            if not choice_id:
                continue
            answer = Choice.objects.get(pk=choice_id)
            quizattempt.chosen_choice = answer
            quizattempt.is_submitted = True
            quizattempt.save()
            if answer.is_correct:
                score += 1
        user.score = score
        user.save()
        
        return redirect("programing_question")


class ProgramingQuestionView(LoginRequiredMixin, TemplateView):
    template_name = "programing_template.html"

    def get_login_url(self) -> str:
        return reverse_lazy("login")

    def get(self, request):
        submission = Submission.objects.filter(user=request.user)
        if not submission:
            easy_question = (
                ProgramingQuestion.objects.filter(difficulty="EASY")
                .order_by("?")
                .first()
            )
            medium_question = (
                ProgramingQuestion.objects.filter(difficulty="MEDIUM")
                .order_by("?")
                .first()
            )
            Submission.objects.get_or_create(user=request.user, question=easy_question)
            Submission.objects.get_or_create(
                user=request.user, question=medium_question
            )

        submission = submission.filter(is_submitted=False).first()
        if not submission:
            self.template_name = "result.html"
            return self.render_to_response(context={})

        context = {
            "question": submission.question.question_file.read().decode("utf-8"),
            "question_obj": submission.question,
        }

        return self.render_to_response(context=context)

    def post(self, request):
        user_code = request.POST.get("user_code", "")
        question_id = request.POST.get("question")
        submit = request.POST.get("submit", "run")

        submission = Submission.objects.filter(
            user=request.user, question=question_id
        ).first()

        submission.user_code.delete()
        submission.user_code.save("user_code.c", ContentFile(user_code), save=True)
        err, score = self.process_submission(submission)
        if submit == "run":
            context = {
                "error": err if err else "",
                "score": score,
                "question": submission.question.question_file.read().decode("utf-8"),
                "question_obj": submission.question,
                'user_code':user_code
            }
            print(user_code)
            return self.render_to_response(context)

        submission.is_submitted = True
        request.user.score += score
        request.user.save()
        submission.save()
        return redirect("programing_question")

    def process_submission(self, submission: Submission):
        file_path = submission.user_code.name
        shared_filepath = file_path.split("/")[-1].replace(".c", ".dll")
        
        compile_command = f"gcc -shared -fPIC -o '{shared_filepath}' -rdynamic {file_path}"
        platform = os.name
        if platform == 'nt':
            compile_command = f"./tcc/tcc -shared -fPIC -o '{shared_filepath}' -rdynamic {file_path}"
        p = subprocess.run(
            shlex.split(compile_command),
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
        )

        if p.returncode != 0:
            err = str(p.stderr).split(":")[-1].strip()
            return err, 0

        test_module_name = submission.question.testcases.name
        test_module = SourceFileLoader("testcases", test_module_name).load_module()
        Test = test_module.TestCase("./" + shared_filepath)
        err, score = Test.run()
        return err, score
