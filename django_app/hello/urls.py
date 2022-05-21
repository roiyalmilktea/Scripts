from django.urls import path
from . import views
#from .views import HelloView

urlpatterns = [
    # path('', views.start, name='form'),  # 本当はindex
    path('xss', views.xss, name='xss'),
    path('next', views.next, name='next'),
    path('forms', views.forms, name='forms'),
    path('problem', views.problem, name='test_problem'),
    path('bufferoverflow', views.bufferoverflow, name='bufferoverflow'),


]
