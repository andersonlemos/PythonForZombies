#coding: utf-8

from bottle import route,run,debug

def italico(f):
    def envelope():
        return '<i>' + f() + '</i>'
    return envelope()

def negrito(f):
    def envelope():
        return '<b>' + f() + '<i>'
    return envelope()

@italico
def outra():
    return 'Outra Página!'

@negrito
def home():
    return 'Home Page'


@route('/')
def home_page():
    return home

@route('/outra')
def outra_page():
    return  outra

debug(True)
run(host='localhost',port=8080)

