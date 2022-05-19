from django.urls import path
from . import views
#from .views import HelloView

urlpatterns = [
    # path('', views.start, name='form'),  # 本当はindex
    path('xss', views.xss, name='xss'),
    path('index2', views.index2, name='index2'),
    path('forms', views.forms, name='forms'),
    path('problem', views.problem, name='test_problem'),
    path('bufferoverflow', views.bufferoverflow, name='bufferoverflow'),


]
