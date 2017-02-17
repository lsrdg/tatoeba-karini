import webbrowser 
from sys import argv

script, command, flang, tlang, term = argv

fRef = '&from='
tRef = '&to='

search = term + fRef + flang + tRef + tlang


if command == 'b':
    webbrowser.open('https://tatoeba.org/eng/sentences/search?query=' + search, new=2)

else:
    print ("Ooops!")

