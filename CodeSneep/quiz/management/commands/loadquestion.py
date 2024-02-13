import json
from quiz.models import Question,Choice


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command description'

    fixture = json.load(open('/workspaces/CodeSneep/CodeSneep/quiz/fixtures/questions.json'))
    questions = []
    choices = []
    def handle(self, *args, **options):
        for data in self.fixture:
            field = data['fields']
            question = Question(
                difficulty = field['difficulty'],
                text = field['text']
            )            
            self.questions.append(question)
        Question.objects.bulk_create(self.questions)
