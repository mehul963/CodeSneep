from django.urls import path
from quiz.views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',QuizView.as_view(),name='quiz'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name = 'login.html',next_page='/'),name='login'),
    path('logout/',LogoutView.as_view(next_page='/login/'),name='logout'),
    path('question/',ProgramingQuestionView.as_view(),name='programing_question'),
]