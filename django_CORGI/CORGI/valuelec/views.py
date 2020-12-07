
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from . import models
from .models import Valuelec_register, Lecture
from .forms import Valuelec_registerForm, LectureForm
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
        print(q_word)
        if q_word:
            object_list = Lecture.objects.filter(lec_name__icontains=q_word)
            print("####################")
            print(object_list)
        else:
            object_list = Lecture.objects.all()
        return object_list

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
            form.save()
            return redirect('valuelec:search_subject')
    else:
        form = Valuelec_registerForm()
    return render(request, 'valuelec_template/entries/register-value.html', {'form': form})

def subject(request):
    form = Valuelec_registerForm()
    return render(request, 'valuelec_template/entries/subject.html', {'form': form})


# def showvalue(request,the_class_id):
#     template_name = "valuelec_template/entries/valuelist.html"
#     values = get_object_or_404(Lecture,pk=the_class_id)
#     context = {"values":values}
#     return render(request,template_name,context)

class showvalue(generic.DetailView):
    model = Lecture
    template_name = "valuelec_template/entries/valuelist.html"
