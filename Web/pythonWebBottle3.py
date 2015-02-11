__author__ = 'anderson'
import bottle
templates_path='./templates/'
@bottle.route('/')
def home_page():
    myThings = ['Python', 'Ruby', 'Perl', 'C++', 'Outra']
    return bottle.template(templates_path + 'hello_world', {'username': 'Masanori',
                                                       'things' : myThings})
@bottle.post('/favorita')
def favorita():
    lang = bottle.request.forms.get('lang')
    if (lang == None or lang == ''):
        lang = 'Nenhuma Escolhida'
    return bottle.template(templates_path + 'lang_selection', {'lang': lang})

bottle.debug(True)
bottle.run(host='localhost', port=8080)