#! /usr/bin/env python#! /usr/bin/env python
# coding: utf-8

import urllib
pagina = urllib.urlopen('http://beans.itcarlow.ie/prices.html')
texto = pagina.read().decode('utf8')
print texto