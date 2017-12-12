import webbrowser, argparse, sys, os, csv, requests, bs4, lxml, tarfile

# Set commanline argments

parser = argparse.ArgumentParser()

parser.add_argument("-b", help="Open a browser and show the result", nargs=3)

parser.add_argument("-d", help="Download files from Tatoeba.org in order to \
        perform offline searchs", nargs=1)

parser.add_argument("-f", help="Find sentence containing term in a specific \
        language", nargs=2)

parser.add_argument("-i", help="Open Tatoeba on the browser searching by \
        sentence's ID", nargs=1)

parser.add_argument("-l", help="List languages and their abbreviation used by \
        Tatoeba", nargs=1)

parser.add_argument("-r", help="Request data from Tatoeba.org, works as the \
        main search on the homepage", nargs=3)

parser.add_argument("-s", help="Search for sentences containing term in a \
        specific language and it the counterparts of the sentence in another \
        language", nargs=3)

args = parser.parse_args()



# --------------------------
# find and store real path

realPath = os.path.dirname(os.path.realpath(__file__))

# --------------------------
# Functions for the main LOCAL search

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
        global translationsList
            
        inLanguageS = args.s[0]
        toLanguageS = args.s[1]
        termInArgS = args.s[2]

        for row in sentencesList:
            if row[1] == inLanguageS and termInArgS in row[2]:
                sentences.append(row)
                findTranslation(row[0])


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

def argD():
    downloadFile = args.d[0]
    def downloadTool():
        with open(realPath + downloadFile + '.tar.bz2', 'wb') as theFile:
            print('Downloading the ', downloadFile, 'file, in the \'.tar.bz2\' format.')
            print('Please wait.')
            res = requests.get('http://downloads.tatoeba.org/exports/' + downloadFile + '.tar.bz2')
            res.raise_for_status()
            if not res.ok:
                print('Download failed.')
                pass

            for block in res.iter_content(1024):
                theFile.write(block)

            print('Download finished.\n\n')

    def uncompressTool():
        print('\n\nUncompressing the', downloadFile, 'file. Please wait.')
        untarFile = tarfile.open(realPath + downloadFile + '.tar.bz2', 'r:bz2')
        untarFile.extractall(realPath)
        untarFile.close()
        print('File uncompressed and ready to use.\n')

    
    if args.d[0] == 'sentences' or args.d[0] == 'links':
        pass
    elif args.d[0] != 'sentences' or args.d[0] != 'links':
        print("Wrong file name. Please, choose between 'sentences' and 'links'.")
        print("Consult the README file to learn more about their usage.")
        return

    print("\nYou will be downloading this file directly from https://tatoeba.org/eng/downloads.")
    print('Keep in mind that this file is released under CC-BY.')
    print('But if you would like more information about the file, check the link above.')
    print('You should also keep in mind that this file can be around 100mb.')
    print('\nThe file will be downloaded and uncompressed.')
    print('\n\nWould you like to proceed? (y/n)')
    
    askForDownload = input('> ')

    if askForDownload.lower() == 'yes' or askForDownload.lower() == 'y':
        downloadTool()
        uncompressTool()


    else:
        print('\n\nNo problems. You can always download and extract the files manually.')
        print('Just head to https://tatoeba.org/eng/downloads.\n')

def argI():
    """
    Open Tatoeba.org in a new tab searching by sentence's ID, just in case.
    Use it to get more information about the sentence.
    """
    sentenceID = args.i[0]
    webbrowser.open('https://tatoeba.org/eng/sentences/show/' + sentenceID, new=2)


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

# Fetching
def argR():

    fromLanguage = args.r[0]
    toLanguage = args.r[1]
    term = args.r[2]
    fromReference = 'from='
    toReference = '&to='
    query = '&query='

    # Join everything to perform the search
    search = fromReference + fromLanguage + toReference + toLanguage + query + term 
    res = requests.get('https://tatoeba.org/eng/sentences/search?', search)
    res.raise_for_status()

    ttbksoup = bs4.BeautifulSoup(res.text, 'lxml')
    elements = ttbksoup.find_all('div', class_='sentence translations'.split())
    print("\n".join("{}".format(el.find('div', class_='text').get_text()) for \
            el in elements), '\n')

    try:
        pagination = ttbksoup.find('md-icon', class_='next')
        pagination = pagination.find('a', href=True)
        nextPage = input("Next page? (y/n) ")
        if nextPage == "y":
            pageURL = pagination['href']
            resNext = requests.get('https://tatoeba.org', pageURL)
            res.raise_for_status()

            ttbksoup = bs4.BeautifulSoup(res.text, 'lxml')
            elements = ttbksoup.find_all('div', class_='sentence translations'.split())
            print("\n".join("{}".format(el.find('div', class_='text').get_text()) for \
                    el in elements), '\n')
        else:
            pass


    except:
        pass
        

def argS():
    findTermTranslatedtoLang()

# --------------------------
# Define command line menu function

def main():

    # Set commanline argments

    parser = argparse.ArgumentParser()

    parser.add_argument("-b", help="Open a browser and show the result", nargs=3)

    parser.add_argument("-d", help="Download files from Tatoeba.org in order to \
            perform offline searchs", nargs=1)

    parser.add_argument("-f", help="Find sentence containing term in a specific \
            language", nargs=2)

    parser.add_argument("-i", help="Open Tatoeba on the browser searching by \
            sentence's ID", nargs=1)

    parser.add_argument("-l", help="List languages and their abbreviation used by \
            Tatoeba", nargs=1)

    parser.add_argument("-r", help="Request data from Tatoeba.org, works as the \
            main search on the homepage", nargs=3)

    parser.add_argument("-s", help="Search for sentences containing term in a \
            specific language and it the counterparts of the sentence in another \
            language", nargs=3)

    args = parser.parse_args()

    if args.b:
        argB()

    elif args.f:
        argF()

    elif args.d:
        argD()

    elif args.i:
        argI()

    elif args.l:
        searchPattern = args.l[0]
        argL(searchPattern)

    elif args.r:
        argR()

    elif args.s:
        argS()


    else:
        print ("Ooops!")


# ---------------------------
# call the main

if __name__ == '__main__':
    main()
