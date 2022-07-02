from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloAnswer
#from .forms import InputForm
from django.http import request
from .models import Friend
import sqlite3

# Create your views here.
# HttpResponse　クラスをimportする


def index(request):
    data = Friend.object.all()
    params = {
        'title': 'Hello',
        'message': 'all friends.',
        'data': 'data',
    }
    return render(request, 'hello/index.html', params)


def start(request):
    params = {
        'title': 'top page',
        'goto_0': 'test_problem',
        'goto_1': 'bufferoverflow',
        'goto_2': 'xss',
    }

    return render(request, 'hello/top.html', params)

###########################################################################################


def xss(request):
    params = {
        'title': 'val',
        'input': 'strings'

    }
    return render(request, 'hello/click.html', params)

##################################################################################################


class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello!',
            'message': 'your data',
            'form': HelloAnswer(),
            'result': None
        }

    def get(self, request):
        return render(request, 'hello/form.html', self.params)

    def post(self, request):
        msg = 'name:'+request.POST['name'] + ' mail:' + \
            request.POST['mail']+' other:'+request.POST['other']

        ch = request.POST['choice']
        self.params['result'] = 'selected:"' + ch + '".'

        # 2922/5/24　messageというパラメータを渡すはずが、forms.htmlでmsgにしていたからエラーになった
        self.params['message'] = msg

        self.params['form'] = HelloAnswer(request.POST)

        return render(request, 'hello/form.html', self.params)


##########################################################################################################


def problem(request):
    params = {
        'title': 'list',
        'msg': 'test',
        'goto_1': 'bufferoverflow',
        'goto_2': 'xss_1',
        'goto_3': 'xss_2',
    }
    return render(request, 'hello/problem.html', params)


def bufferoverflow(request):
    def func():
        params = {
            'title': 'You must learn C lang.',
            'goto': 'c_lang'
        }
        return render(request, 'hello/c_lang.html', params)

##########################################################################################################
