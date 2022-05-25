from django.urls import path
from django.conf.urls import url
from . import views
from .views import HelloView

urlpatterns = [
    # path('', views.start, name=''),  # 本当はindex
    #path('next', views.next, name='next'),
    path('forms', views.forms, name='forms'),
    path('problem', views.problem, name='test_problem'),
    path('bufferoverflow', views.bufferoverflow, name='bufferoverflow'),
    url(r'', HelloView.as_view(), name='forms'),

]
