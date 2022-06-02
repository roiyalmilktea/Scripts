from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from django.http import request
#from .reflect import Route
#from .forms import HelloAnswer


# Create your views here.
# HttpResponse　クラスをimportする


def start(request):
    params = {
        'title': 'top page',
        'goto_0': 'test_problem',
        'goto_1': 'bufferoverflow',
        # 'goto_2': 'xss',
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
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/forms.html', self.params)

    def post(self, request):
        msg = 'name:'+request.POST['name'] + ' mail:' + \
            request.POST['mail']+' other:'+request.POST['other']

        # 2922/5/24　messageというパラメータを渡すはずが、forms.htmlでmsgにしていたからエラーになった
        self.params['message'] = msg

        self.params['form'] = HelloForm(request.POST)

        return render(request, 'hello/forms.html', self.params)


##########################################################################################################


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

##########################################################################################################


def reflect(request):
    username = request.query.get('user')
    username = '' if username is None else username
    html = "<h2>Hello{name}</h2>".format(name=username)

    return render(request, html)
