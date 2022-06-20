# -*- coding:utf-8 -*-
from bottle import route
from bottle import run
from bottle import request
import html


@route('/')
def func(user=''):

    username = request.query.get('user')
    username = '' if username is None else username
    # code

    body = "<h2> Hello {name} </h2>".format(name=username)
    return body


run(host='localhost', port=5000, debug=True)
