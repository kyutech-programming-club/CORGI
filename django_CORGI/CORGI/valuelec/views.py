from django.shortcuts import render
from .models import serch
from django.views.generic import ListView

# Create your views here.
def index_render(request):
    return render(request, 'valuelec_template/entries/index.html')

def serch_subject(request):
    return render(request,'valuelec_template/entries/serch_subject.html')

def explain(request):
    return render(request,'valuelec_template/entries/explain.html')

