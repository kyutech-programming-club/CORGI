from django.shortcuts import render, redirect
#from .models import search,
from django.views.generic import ListView
from .models import Valuelec_register, Lecture
from .forms import Valuelec_registerForm, LectureForm
from django.urls import reverse_lazy

# Create your views here.
def index_render(request):
    return render(request, 'valuelec_template/entries/index.html')

def search_subject(request):
    return render(request, 'valuelec_template/entries/search_subject.html',)

class search_subject_view(ListView):
    model = Lecture
    template_name = 'valuelec_template/entries/search_subject.html'
    success_url = reverse_lazy('subject')

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
