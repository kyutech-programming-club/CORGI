from django import forms

from .models import Valuelec_register, Lecture

class Valuelec_registerForm(forms.ModelForm):

    class Meta:
        model = Valuelec_register
        fields = (
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
