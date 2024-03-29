# Generated by Django 5.0.1 on 2024-02-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0008_programingquestion_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="difficulty",
            field=models.CharField(
                choices=[("EASY", "Easy"), ("MEDIUM", "Medium"), ("HARD", "Hard")],
                default="EASY",
                max_length=15,
            ),
            preserve_default=False,
        ),
    ]
