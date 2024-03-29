# Generated by Django 5.0.1 on 2024-02-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0009_question_difficulty"),
    ]

    operations = [
        migrations.AddField(
            model_name="programingquestion",
            name="difficulty",
            field=models.CharField(
                choices=[("EASY", "Easy"), ("MEDIUM", "Medium"), ("HARD", "Hard")],
                default="EASY",
                max_length=15,
            ),
            preserve_default=False,
        ),
    ]
