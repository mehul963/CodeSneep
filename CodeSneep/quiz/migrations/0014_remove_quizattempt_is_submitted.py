# Generated by Django 5.0.1 on 2024-02-06 12:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0013_quizattempt_is_submitted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quizattempt",
            name="is_submitted",
        ),
    ]
