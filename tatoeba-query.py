import webbrowser
from sys import argv

script, browser, flang, tlang, term = argv

fRef = '&from='
tRef = '&to='

search = term + fRef + flang + tRef + tlang

if browser == 'browser':
    webbrowser.open('https://tatoeba.org/eng/sentences/search?query=' + search, new=2)
else:
    print ("Ooops!")
