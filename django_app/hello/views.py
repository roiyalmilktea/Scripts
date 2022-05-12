from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .forms import HelloAnswer
# Create your views here.
# HttpResponse　クラスをimportする


def start(request):
    params = {
        'title': 'top page',
        'goto_0': 'test_problem',
        'goto_1': 'bufferoverflow',
        'goto_2': 'xss'
    }

    return render(request, 'hello/top.html', params)

###########################################################################################


def index2(request):
    params = {
        'title': 'Hello!',
        'message': 'What you are data？',
        'form': HelloForm()
    }
    if (request.method == 'POST'):
        params['message'] = 'name:'+request.POST['name']+'<br>mail:' + \
            request.POST['mail']+'<br>age:' + \
            request.POST['age']+'<br>job:'+request.POST['job']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index2.html', params)


def forms(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': 'hello!' + msg,
    }
    return render(request, 'hello/index2.html', params)

#################################################################################################################################


def problem(request):
    params = {
        'title': 'list',
        'msg': 'test',
        'goto_1': 'bufferoverflow',
        'goto_2': 'xss',
    }
    return render(request, 'hello/problem.html', params)


def bufferoverflow(request):
    params = {
        'title': 'You must learn C lang.',
        'goto': 'c_lang'
    }
    return render(request, 'hello/c_lang.html', params)


def xss(request):
    params = {
        'title': 'web',
        'goto': 'xss'
    }
    return render(request, 'hello/reflected_xss.html', params)
