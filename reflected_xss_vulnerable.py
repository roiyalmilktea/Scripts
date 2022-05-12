# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request
import html


@route('/')
def hello(user=''):
    username = request.query.get('user')
    username = '' if username is None else username
    # エスケープ処理を施す必要がある
    username = html.escape(username)

    body = "<h2> Hello {name} </h2>".format(name=username)

   # html = "<h2> Hello {name} </h2>".format(name=username)
    return body


run(host='localhost', port=8080, debug=True)
