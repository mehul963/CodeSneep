from django.contrib import admin
from django.http.request import HttpRequest
from quiz.models import *
# Register your models here.
from django.contrib import admin
from .models import Question, Choice, QuizAttempt

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    
class QuizAttemptModel(admin.ModelAdmin):
    list_display = ["user","question","chosen_choice",'get_correct']
    def get_correct(self, obj):
        if obj.chosen_choice:
            return obj.chosen_choice.is_correct
    get_correct.short_description = 'Choosen is correct or not'  # Set column name in admin panel

class QuizAttemptInline(admin.TabularInline):
    model = QuizAttempt
    list_display = ["user","question","chosen_choice",'get_correct']
    def get_correct(self, obj):
        if obj.chosen_choice:
            return obj.chosen_choice.is_correct

    get_correct.short_description = 'Choosen is correct or not'

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    readonly_fields = list_display
    extra = 0
    
    def has_add_permission(self, request: HttpRequest,obj=None) -> bool:
        return False
    def has_delete_permission(self, request: HttpRequest,obj=None) -> bool:
        return False
    def has_change_permission(self, request: HttpRequest,obj=None) -> bool:
        return False

class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 0
    
    def has_add_permission(self, request: HttpRequest,obj=None) -> bool:
        return False
    def has_delete_permission(self, request: HttpRequest,obj=None) -> bool:
        return False
    def has_change_permission(self, request: HttpRequest,obj=None) -> bool:
        return False
    
class UserAdmin(admin.ModelAdmin):
    inlines = [QuizAttemptInline,SubmissionInline]
    list_display = 'username','first_name','last_name','score'
    

admin.site.register(User,UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(ProgramingQuestion)
admin.site.register(QuizAttempt,QuizAttemptModel)
