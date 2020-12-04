from django.shortcuts import render, redirect
from django.db import models
from . import models
from .models import Valuelec_register, Lecture
from .forms import Valuelec_registerForm, LectureForm
from django.urls import reverse_lazy
from django.http import Http404

# Create your views here.
def index_render(request):
    return render(request, 'valuelec_template/entries/index.html')

def search_subject(request):
    context= {'classes':models.Lecture.objects.all()}
    return render(request, 'valuelec_template/entries/search_subject.html', context)

def explain(request):
    return render(request,'valuelec_template/entries/explain.html')

def registerclass(request):
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('valuelec:subject')
    else:
        form = LectureForm()
    return render(request, 'valuelec_template/entries/register-class.html', {'form': form})

def subject(request):
    form = Valuelec_registerForm()
    return render(request, 'valuelec_template/entries/subject.html', {'form': form})


def showvalue(request,lec_name_for_url):
    template_name = "valuelec_template/entries/test.html"
    try:
        values = models.Lecture.objects.get(lec_name_for_url=lec_name_for_url)
    except models.Lecture.DoesNotExist:
        raise Http404
    context = {"values":values}
    return render(request,template_name,context)
