from django.urls import path
from django.conf.urls import url
from . import views
from .views import HelloView

urlpatterns = [
    path('start', views.start, name=''),  # 本当はindex

    path('xss', views.xss, name='xss'),
    path('problem', views.problem, name='test_problem'),
    path('bufferoverflow', views.bufferoverflow, name='bufferoverflow'),
    url(r'', HelloView.as_view(), name='forms'),
    path('index', views.index, name='index'),

]
