from django.urls import path

from . import views

app_name = 'valuelec'

urlpatterns = [
    path('', views.index_render, name='index_render'),
    path('search_subject/', views.search_subject.as_view(), name='search_subject'),
    path('explain/', views.explain, name='explain'),
    path('registerclass/', views.registerclass, name='registerclass'),
    path('subject/', views.subject, name='subject'),
    path('subject/<int:pk>/',views.showvalue.as_view(),name='showvalue'),
    path('subject/register/',views.registervalue, name='registervalue'),
    path('question/registerquestion/',views.registerquestion,name='registerquestion'),
    path('question/',views.question.as_view(),name='question'),
    path('question/<int:pk>/',views.questiondetail.as_view(),name='questiondetail'),
    path('question/registeranswer/',views.registeranswer,name='registeranswer'),
]
