from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloAnswer
from .forms import HelloSearch
from django.http import request
from .models import Friend
import sqlite3

# Create your views here.
# HttpResponse　クラスをimportする


def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'all friends list.',
        'form': HelloSearch(),
        'data': data,

    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloSearch(request.POST)
    else:
        params['data'] = Friend.objects.all()

    return render(request, 'hello/index.html', params)

###########################################################################################


def start(request):
    params = {
        'title': 'top page',
        'goto_0': 'test_problem',
        'goto_1': 'bufferoverflow',
        'goto_2': 'xss',
    }

    return render(request, 'hello/top.html', params)

###########################################################################################


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

        ch = request.POST['choice']
        self.params['result'] = 'selected:"' + ch + '".'

        # 2922/5/24　messageというパラメータを渡すはずが、forms.htmlでmsgにしていたからエラーになった
        #self.params['form'] = HelloAnswer(request.POST)
        self.params['message'] = HelloAnswer(request.POST)

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

    params = {
        'title': 'You must learn C lang.',
        'goto': 'c_lang'
    }
    return render(request, 'hello/c_lang.html', params)

##########################################################################################################
