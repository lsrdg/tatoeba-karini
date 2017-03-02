import webbrowser, argparse, sys, os, csv 

# Set commanline argments

parser = argparse.ArgumentParser()

parser.add_argument("-b", help="Open a browser and show the result", nargs=3)
parser.add_argument("-f", help="Find sentence containing term in a specific language", nargs=2)
parser.add_argument("-l", help="List languages and their abbreviation used by Tatoeba", nargs=1)
parser.add_argument("-s", help="Search for sentences containing term in a \
        specific language and it the counterparts of the sentence in another language", nargs=3)

args = parser.parse_args()

# --------------------------
# find and store real path

realPath = os.path.dirname(os.path.realpath(__file__))

# --------------------------
# Functions for the main search

# The main search stuff

sentences = []
translationsList = []
def findTranslation(register):
    global translationID
    global toLanguage
    global translationsList
    global testUhuList
    global testCheckID

    with open(realPath + '/links.csv') as links:
        linksList = csv.reader(links, delimiter='\t')

        for line in linksList: 
            if line[0] == register:
                testCheckID = line[1]
                checkTranslation(testCheckID)
                continue
            else:
                pass

def checkTranslation(possibleID):
    global sentences
    global translationsList

    inLanguageS = args.s[0]
    toLanguageS = args.s[1]
    termInArgS = args.s[2]

    with open(realPath + '/sentences.csv') as sentencesListing:
        sentencesList = csv.reader(sentencesListing, delimiter='\t')
        for row in sentencesList:
            if row[0] == possibleID and toLanguageS == row[1]:
                translationsList.append(row)
                print(sentences[-1])
                print(translationsList[-1], '\n\n')
                continue
            else:
                pass

def findTermTranslatedtoLang():
    with open(realPath + '/sentences.csv') as sentencesListing:
        sentencesList = csv.reader(sentencesListing, delimiter='\t')
        global sentences
        global baseID
        global translationsList
        global baseRow
            
        inLanguageS = args.s[0]
        toLanguageS = args.s[1]
        termInArgS = args.s[2]

        for row in sentencesList:
            if row[1] == inLanguageS and termInArgS in row[2]:
                baseID = row[0]
                baseRow = row
                sentences.append(baseRow)
                findTranslation(baseID)


            elif row[1] != inLanguageS or termInArgS not in row[2]:
                pass
# Define argument function

def argB():
    # Open tatoeba.org in a new tab browser performing a search
    
    # ArgB variables
    fromLanguage = args.b[0]
    toLanguage = args.b[1]
    term = args.b[2]
    fromReference = '&from='
    toReference = '&to='

    # Join everything to perform the search
    search = term + fromReference + fromLanguage + toReference + toLanguage
    
    # Open the browser
    webbrowser.open('https://tatoeba.org/eng/sentences/search?query=' + search, new=2)

def argF():

    # Make use of the 'sentences.csv' file to to find a sentence containing 
    # a term in an language
    
    # argF variables
    inLanguageF = args.f[0]
    termInArgF = args.f[1]
    with open(realPath + '/sentences.csv') as listFile:
        readList = csv.reader(listFile, delimiter='\t')


        # function responsible for making the search AND looping the matches
        def findTermInLang():
            foundedTerm = [
                    row 
                    for row in readList
                    if row[1] == inLanguageF and termInArgF in row[2]
                    ]

            for row in foundedTerm:
                print(row)

        
        findTermInLang()

def argL():
    searchPattern = args.l[0]
    with open(realPath + '/abbreviationList.csv') as abbreviationList:
        abbList = csv.reader(abbreviationList, delimiter='\t')
        abbreviation = [row for row in abbList if searchPattern in row]
        print(abbreviation)

def argS():
    findTermTranslatedtoLang()

# --------------------------
# Define command line menu function

def menuInit():

    if args.b:
        argB()

    elif args.f:
        argF()

    elif args.l:
        argL()

    elif args.s:
        argS()

    else:
        print ("Ooops!")

#---------------------------
# call the menu

menuInit()
