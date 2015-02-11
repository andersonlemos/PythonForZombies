__author__ = 'anderson'
import bottle

@bottle.route('/')
def home_page():
    myThings = ['Python', 'Ruby', 'Perl', 'C++']
    return bottle.template('./templates/hello_world', {'username': 'Masanori',
                                                       'things': myThings})
@bottle.post('/favorita',)
def favorita():
    lang = bottle.request.forms.get('lang')
    if (lang == None or lang == ''):
        lang = 'Nenhuma Escolhida'
    return bottle.template('./templates/lang_selection', {'lang': lang})

bottle.debug(True)
bottle.run(host='localhost', port=8080)