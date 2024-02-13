from django import forms
from quiz.models import User
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username','first_name','last_name','email','password'