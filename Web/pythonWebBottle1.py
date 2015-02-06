#coding: utf-8

from bottle import route, run, debug


@route('/')
def home_page():
    return 'Alô minha primeira rota'


@route('/outra')
@italico
def test_page():
    return 'Outra página zumbi'

debug(True)
run(host='localhost', port=8080)