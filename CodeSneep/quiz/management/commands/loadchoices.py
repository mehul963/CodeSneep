import json
from quiz.models import Question,Choice


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command description'

    fixture = json.load(open('/workspaces/CodeSneep/CodeSneep/quiz/fixtures/questions.json'))
    choices = []
    def handle(self, *args, **options):
        for data in self.fixture:
            field = data['fields']
            question = Question.objects.get(pk=data['pk'])
            choices = field['choices']
            for choice in choices:
                self.choices.append(
                    Choice(
                        question = question,
                        text = choice['text'],
                        is_correct = choice['is_correct']
                    )
                )

        Choice.objects.bulk_create(self.choices)