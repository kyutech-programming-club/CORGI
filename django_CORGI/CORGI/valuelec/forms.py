from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Valuelec_register, Lecture, Question, Answer
from django.contrib.auth.models import User

class signupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not '@mail.kyutech.jp' in email:
            raise forms.ValidationError(u'有効なメールアドレスではありません')
            return email

class Valuelec_registerForm(forms.ModelForm):

    class Meta:
        model = Valuelec_register
        fields = (
            'the_class',
            'total_evaluation',
            'lec_simplicity',
            'credit_simplicity',
            'task_smallness',
            'class_style',
            'comment',
        )

class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = (
            'lec_name',
            'teacher_name',
        )

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = (
            'question_id',
            'question',
        )

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = (
            'answer_id',
            'answer'
        )
