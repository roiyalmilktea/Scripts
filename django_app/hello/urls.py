from django.urls import path
from . import views
#from .views import HelloView

urlpatterns = [
    path('', views.start, name='form'),  # 本当はindex
    path('next', views.next, name='next'),
    path('index2', views.index2, name='index2'),
    path('forms', views.forms, name='forms'),
    path('problem', views.problem, name='problem'),
    #path('prblem_1', views.problem_1, name='forms'),

]
