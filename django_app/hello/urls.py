from django.urls import path
from django.conf.urls import url
from . import views
from .views import HelloView

urlpatterns = [
    path('start', views.start, name=''),  # 本当はindex
    path('problem', views.problem, name='test_problem'),
    path('bufferoverflow', views.bufferoverflow, name='bufferoverflow'),
    url('helloview', HelloView.as_view(), name='forms'),
    path('', views.index, name='index'),

]
