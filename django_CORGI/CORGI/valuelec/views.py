from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from . import models
from .models import Valuelec_register, Lecture, Question, Answer
from .forms import Valuelec_registerForm, LectureForm, QuestionForm, AnswerForm
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic


# Create your views here.
def index_render(request):
    return render(request, 'valuelec_template/entries/index.html')

class search_subject(generic.ListView):
    model = Lecture
    template_name = 'valuelec_template/entries/search_subject.html'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Lecture.objects.filter(lec_name__icontains=q_word)
        else:
            object_list = Lecture.objects.all()
        return object_list.order_by('-id')

def explain(request):
    return render(request,'valuelec_template/entries/explain.html')

def registerclass(request):
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('valuelec:search_subject')
    else:
        form = LectureForm()
    return render(request, 'valuelec_template/entries/register-class.html', {'form': form})

def registervalue(request):
    if request.method == "POST":
        form = Valuelec_registerForm(request.POST)
        if form.is_valid():
            registercomment = form.cleaned_data['the_class']
            commentlist = str(registercomment).split()
            comment = Lecture.objects.get(lec_name__icontains=commentlist[0], teacher_name__icontains=commentlist[1])
            commentid = comment.id
            form.save()
            return redirect('valuelec:showvalue', commentid)
    else:
        form = Valuelec_registerForm()
    return render(request, 'valuelec_template/entries/register-value.html', {'form': form})

def subject(request):
    form = Valuelec_registerForm()
    return render(request, 'valuelec_template/entries/subject.html', {'form': form})

class showvalue(generic.DetailView):
    model = Lecture
    template_name = "valuelec_template/entries/valuelist.html"

class question(generic.ListView):
    queryset = Question.objects.order_by('-id')
    template_name = "valuelec_template/entries/question-list.html"

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Question.objects.filter(question_id__lec_name__icontains=q_word)
        else:
            object_list = Question.objects.all()
        return object_list.order_by('-id')

def registerquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('valuelec:question')
    else:
        form = QuestionForm()
    return render(request, 'valuelec_template/entries/register-question.html', {'form': form})

class questiondetail(generic.DetailView):
    queryset = Question.objects.order_by('-id')
    template_name  = 'valuelec_template/entries/answer.html'

def registeranswer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            questioncomment = form.cleaned_data['answer_id']
            question = Question.objects.get(question__icontains=questioncomment)
            questionid = question.id
            form.save()
            return redirect('valuelec:questiondetail', questionid)
    else:
        form = AnswerForm()
    return render(request, 'valuelec_template/entries/register-answer.html', {'form': form})
