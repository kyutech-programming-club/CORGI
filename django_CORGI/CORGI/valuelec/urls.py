from django.urls import path

from . import views

app_name = 'valuelec'

urlpatterns = [
    path('', views.index_render, name='index_render'),
]
