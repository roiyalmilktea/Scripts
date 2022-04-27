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
        'goto': 'problem',

    }

    return render(request, 'hello/top.html', params)


def index(request):
    params = {

        'title': '#Reversing security',
        'message': '・コンピュータアーキテクチャを解析し、アセンブリを読み取る',
        'tema1': 'バイナリ解析',
        'tema2': 'コンピュータハイジャッキング',
        'tema3': 'ghidra',
        'tema4': 'x86-64',
        'next_page': '次のページ',
        'site': 'https://google.com/',
        'goto': 'next',

    }
    return render(request, 'hello/index.html', params)


def next(request):
    params = {
        'title': '#Web security',
        'message': '・webアプリケーション上の脆弱性を見つける',
        'tema1': 'SQLinjection',
        'tema2': 'XSS',
        'tema3': 'directyreversal',
        'tema4': 'CSRF',
        'next_page': 'regist your imfomation!',
        'site': 'https://google.com/',
        'goto': 'index2',
    }
    return render(request, 'hello/index.html', params)


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


def problem(request):
    params = {
        'title': 'list',
        'msg': 'test',
        'goto': 'problem_0',
    }
    return render(request, 'hello/problem_0.html', params)
