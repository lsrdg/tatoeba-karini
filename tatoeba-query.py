import webbrowser, argparse, sys, os, csv 

# Set commanline argments

parser = argparse.ArgumentParser()

parser.add_argument("-b", help="Open a browser and show the result", nargs=3)
parser.add_argument("-f", help="Find sentence containing term in a specific language", nargs=2)
parser.add_argument("-l", help="List languages and their abbreviation used by Tatoeba", nargs=1)

args = parser.parse_args()

# --------------------------
# find and store real path

realPath = os.path.dirname(os.path.realpath(__file__))

# --------------------------
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
    inLanguage = args.f[0]
    termInArgF = args.f[1]
    listFile = open(realPath + '/sentences.csv')
    readList = csv.reader(listFile, delimiter='\t')


    # function responsible for making the search AND looping the matches
    def findTermInLang():
        for row in readList:
            if row[1] == inLanguage and termInArgF in row[2]:
                print(row)
    
    findTermInLang()

    listFile.close()


# --------------------------
# Define command line menu function

def menuInit():

    if args.b:
        argB()

    elif args.f:
        argF()

    else:
        print ("Ooops!")

#---------------------------
# call the menu

menuInit()
