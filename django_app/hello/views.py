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
        'goto_2': 'xss',
    }

    return render(request, 'hello/top.html', params)

###########################################################################################


def forms(request):
    params = {
        'title': 'Hello!',
        'message': 'input',
        'form': HelloForm()
    }

    if (request.method == 'POST'):
        params['message'] = 'name:'+request.POST['name']+'<br>mail:' + \
            request.POST['mail']+'<br>age:' + \
            '<br>other:'+request.POST['other']
        params['form'] = HelloForm(request.POST)

    return render(request, 'hello/forms.html', params)

####################################################################################################
# nextはまだ使わない


def next(request):

    params = {
        'title': 'submmit',
        'msg': 'name',
        'form': HelloForm(),
        'goto': 'next',
    }

    return render(request, 'hello/done.html', params)

####################################################################################################

# 入力後レスポンスを返した


def responsed(request):
    return render(request, 'done.html')


# def moved(request):


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

    return render(request, 'hello/xss.php')
