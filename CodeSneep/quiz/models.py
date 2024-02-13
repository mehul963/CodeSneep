from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create(self,username,password, **kwargs: Any) -> Any:
        user = self.model(
            username = username,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        user = self.create(username,password,**kwargs)
        return user

class User(AbstractUser):
    score = models.PositiveIntegerField(default=0)
    objects = UserManager()

class Question(models.Model):
    difficulty_level = [
        ('EASY','Easy'),
        ('MEDIUM','Medium'),
        ('HARD','Hard'),
    ]
    difficulty = models.CharField(max_length=15,choices=difficulty_level)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question,related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    is_submitted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username}'s attempt on {self.question}"

class ProgramingQuestion(models.Model):
    
    difficulty_level = [
        ('EASY','Easy'),
        ('MEDIUM','Medium'),
        ('HARD','Hard'),
    ]
    difficulty = models.CharField(max_length=15,choices=difficulty_level)
    title = models.CharField(max_length = 250)
    question_file = models.FileField(upload_to='programingquestions')
    solution_snippet = models.TextField()
    testcases = models.FileField(upload_to='testcases')
    
    def __str__(self) -> str:
        return self.title


class Submission(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(ProgramingQuestion,on_delete=models.CASCADE)
    user_code = models.FileField(upload_to='usercodes',null=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"Submit by {self.user.username} for {self.question}"
