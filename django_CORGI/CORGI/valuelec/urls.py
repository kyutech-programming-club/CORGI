from django.urls import path

from . import views
from .views import serch_subject_view

app_name = 'valuelec'

urlpatterns = [
    path('', views.index_render, name='index_render'),
    path('serch_subject/', serch_subject_view.as_view(), name='serch_subject'),
    path('explain/', views.explain, name='explain'),
    path('registerclass/', views.registerclass, name='registerclass'),
]
