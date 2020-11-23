from django.urls import path

from . import views
from .views import search_subject_view

app_name = 'valuelec'

urlpatterns = [
    path('', views.index_render, name='index_render'),
    path('search_subject/', search_subject_view.as_view(), name='search_subject'),
    path('explain/', views.explain, name='explain'),
    path('registerclass/', views.registerclass, name='registerclass'),
    path('subject/', views.subject, name='subject')
]
