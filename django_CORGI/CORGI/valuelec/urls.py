from django.urls import path

from . import views

app_name = 'valuelec'

urlpatterns = [
    path('', views.index_render, name='index_render'),
    path('serch_subject/', views.serch_subject, name='serch_subject'),
    path('explain/', views.explain, name='explain'),
]
