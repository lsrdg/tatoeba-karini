import webbrowser
import argparse


# from sys import argv

# script, command, flang, tlang, term = argv

parser = argparse.ArgumentParser()

parser.add_argument("-b", help="Open a browser and show the result", nargs=3)

args = parser.parse_args()

fromLanguage = args.b[0]
toLanguage = args.b[1]
term = args.b[2]

fromReference = '&from='
toReference = '&to='

search = term + fromReference + fromLanguage + toReference + toLanguage


if args.b:
    webbrowser.open(
        'https://tatoeba.org/eng/sentences/search?query=' + search, new=2)

else:
    print("Ooops!")
