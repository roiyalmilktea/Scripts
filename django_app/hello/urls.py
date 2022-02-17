from django.urls import path
from . import views
#from .views import HelloView

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('index2', views.index2, name='index2'),
    path('forms', views.forms, name='forms'),

]
