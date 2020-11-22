from django.shortcuts import render
#from .models import serch
from django.views.generic import ListView
from .models import Valuelec_register, Lecture
from .forms import Valuelec_registerForm, LectureForm

# Create your views here.
def index_render(request):
    return render(request, 'valuelec_template/entries/index.html')

def serch_subject(request):
    return render(request, 'valuelec_template/entries/serch_subject.html',)

class serch_subject_view(ListView):
    model = Lecture
    template_name = 'valuelec_template/entries/serch_subject.html'

def explain(request):
    return render(request,'valuelec_template/entries/explain.html')

def registerclass(request):
    form = LectureForm()
    return render(request, 'valuelec_template/entries/register-class.html', {'form': form})
