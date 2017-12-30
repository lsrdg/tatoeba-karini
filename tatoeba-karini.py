import webbrowser
import argparse
import os
import csv
import re
import requests
import bs4
import tarfile


# --------------------------
# find and store real path

realPath = os.path.dirname(os.path.realpath(__file__))

# --------------------------
# Functions for the main LOCAL search

# The main search stuff

sentences = []
translationsList = []


def findTranslation(register, inLanguageS, toLanguageS, termInArgS):
    """
    Make use of the file `links.csv` to check if a sentence has a translation
    in the target language specified by the user.
    """

    with open(realPath + '/links.csv') as links:
        linksList = csv.reader(links, delimiter='\t')

        for line in linksList:
            if line[0] == register:
                testCheckID = line[1]
                checkTranslation(
                    testCheckID, inLanguageS, toLanguageS, termInArgS)
                continue
            else:
                pass


def checkTranslation(possibleID, inLanguageS, toLanguageS, termInArgS):
    """
    Check on the file `sentences.csv` if a translation exists. If it does, it
    will be printed, or else, move on to the next iteration.
    """

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


def findTermTranslatedtoLang(inLanguageS, toLanguageS, termInArgS):
    """
    Takes the user input and checks if there is a sentence containing the
    searched term in the desired source language.

    If there is, move on and call `findTranslation()` to find possible
    translations. If not, pass.
    """

    with open(realPath + '/sentences.csv') as sentencesListing:
        sentencesList = csv.reader(sentencesListing, delimiter='\t')

        for row in sentencesList:
            if row[1] == inLanguageS and termInArgS in row[2]:
                sentences.append(row)
                findTranslation(row[0], inLanguageS, toLanguageS, termInArgS)

            elif row[1] != inLanguageS or termInArgS not in row[2]:
                pass
# Define argument function


def browserWrapper(fromLanguage, toLanguage, term):
    """
    Wrapper to the 'browser' functionality.
    Open tatoeba.org in a new tab browser performing a search
    """

    # ArgB variables
    fromReference = '&from='
    toReference = '&to='

    # Join everything to perform the search
    search = term + fromReference + fromLanguage + toReference + toLanguage

    # Open the browser
    webbrowser.open(
        'https://tatoeba.org/eng/sentences/search?query=' + search, new=2
    )


def downloadWrapper(downloadFile):
    """
    Wrapper for the download functionality.
    Download and uncompress the files needed by the off line search/find
    functionalities.
    """

    def downloadTool():
        """
        Download the `sentences.csv` file or the `links.csv` file.
        """

        with open(realPath + downloadFile + '.tar.bz2', 'wb') as theFile:
            print('Downloading the ',
                  downloadFile, 'file, in the \'.tar.bz2\' format.')
            print('Please wait.')
            res = requests.get('http://downloads.tatoeba.org/exports/' +
                               downloadFile + '.tar.bz2')
            res.raise_for_status()
            if not res.ok:
                print('Download failed.')
                pass

            for block in res.iter_content(1024):
                theFile.write(block)

            print('Download finished.\n\n')

    def uncompressTool():
        """
        Uncompress the downloaded file.
        """

        print('\n\nUncompressing the', downloadFile, 'file. Please wait.')
        untarFile = tarfile.open(realPath + downloadFile + '.tar.bz2', 'r:bz2')
        untarFile.extractall(realPath)
        untarFile.close()
        print('File uncompressed and ready to use.\n')

    if downloadFile == 'sentences' or downloadFile == 'links':
        pass
    elif downloadFile != 'sentences' or downloadFile != 'links':
        print("""
            Wrong file name. Please, choose between 'sentences' and 'links'.
            Consult the README file to learn more about their usage.
              """)
        return

    print("""
            \nYou will be downloading this file directly
            \nfrom https://tatoeba.org/eng/downloads.
            \nKeep in mind that this file is released under CC-BY.
            \nBut if you would like more information about the file,
            \n\ncheck the link above.
            \nYou should also keep in mind that this file can be around 100mb.
            \nThe file will be downloaded and uncompressed.')
            \n\nWould you like to proceed? (y/n)')
           """)

    askForDownload = input('> ')

    if askForDownload.lower() == 'yes' or askForDownload.lower() == 'y':
        downloadTool()
        uncompressTool()

    else:
        print("""
                \n\nNo problems. You can always download and
                extract the files manually.
                Just head to https://tatoeba.org/eng/downloads.
                \n
              """)


def idWrapper(sentenceId):
    """
    Open Tatoeba.org in a new tab searching by sentence's ID, just in case.
    Use it to get more information about the sentence.
    """
    webbrowser.open(
        'https://tatoeba.org/eng/sentences/show/' + sentenceId, new=2
    )


def findWrapper(inLanguageF, termInArgF):
    """
    Wrapper for the `find` functionality.
    Make use of the 'sentences.csv' file to to find a sentence containing
    a term in an language.
    """

    # findWrapper variables
    with open(realPath + '/sentences.csv') as listFile:
        readList = csv.reader(listFile, delimiter='\t')

        def findTermInLang():
            """
            function responsible for making the search AND looping the matches.
            """
            foundedTerm = [
                row
                for row in readList
                if row[1] == inLanguageF and termInArgF in row[2]
            ]

            for row in foundedTerm:
                print(row)

        findTermInLang()


def listAbbreviationWrapper(searchPattern):
    """
    Look for the abbreviation of language.
    Necessary for the off line searches.
    The abbreviations follow Tatoeba's pattern.
    """

    with open(realPath + '/abbreviationList.csv') as abbreviationList:
        abbList = csv.reader(abbreviationList, delimiter='\t')
        abbreviation = [row for row in abbList if searchPattern in row]
        print(abbreviation)


# Fetching
def requestGet(search):
    """
    Returns an object of the get method of requests.
    """

    res = requests.get(search)
    return(res)


def requestPaginationInput(value):
    """
    Return whether the user want to see the next page or not.
    """
    userInput = input(value)
    if userInput == "y":
        return("y")
    elif userInput == "n":
        return("n")
    else:
        return(print('Invalid input.'))


def requestPagination(search):
    """
    Simulate `requestWrapper()`'s behavior in case the user wants to
    paginate the results.
    """
    res = requestGet(search)
    toPrint = requestPrint(res)
    return(toPrint)


def requestPrint(value):
    """
    Wrapper the 'printing' aspects of `requestWrapper()`.
    Print sentences and its translations.
    """

    res = value
    res.raise_for_status()

    ttbksoup = bs4.BeautifulSoup(res.text, 'lxml')
    elements = ttbksoup.find_all('div', class_='sentence translations'.split())

    try:
        pagination = ttbksoup.find('md-icon', class_='next')
        if pagination is None:
            print("\n".join("{}".format(el.find(
                'div', class_='text').get_text()) for el in elements), '\n')
            return(False)
        else:
            print("\n".join("{}".format(el.find(
                'div', class_='text').get_text()) for el in elements), '\n')
            paginationHref = pagination.find('a', href=True)
            return(paginationHref.get('href'))

    except AttributeError:
            pass


def requestWrapper(fromLanguage, toLanguage, term):
    """
    Wrapper for the 'request' functionality.
    Scrap tatoeba.org.

    Support basic forward pagination.
    """

    urlBase = 'https://tatoeba.org'
    searchBase = '/eng/sentences/search?'
    fromReference = 'from='
    toReference = '&to='
    query = '&query='

    # Join everything to perform the search

    search = urlBase + searchBase + fromReference + fromLanguage +\
        toReference + toLanguage + query + term
    res = requestGet(search)

    pagination = requestPrint(res)

    while pagination is not False:
        nextPage = requestPaginationInput('Next page? (y/n) ')
        if nextPage == "n":
            return(print('Ok, no pagination this time...'))
        elif nextPage == "y":
            search = urlBase + pagination
            pagination = requestPagination(search)
    else:
        return


def searchWrapper(inLanguageS, toLanguageS, termInArgS):
    """
    Wrapper for the search functionality, which despite
    of its complexity, is implemented with the use of the
    'find' functionality.
    """

    findTermTranslatedtoLang(inLanguageS, toLanguageS, termInArgS)

# --------------------------
# Define command line menu function


def parse_arguments():
    """
    Parse and return arguments.
    """

    parser = argparse.ArgumentParser("tatoeba-karini [COMMAND] [ARGUMENT(S)]")

    parser.add_argument("--version", "-v", action="version", version="v0.0.5+")

    subparsers = parser.add_subparsers(help="Types of commands")

    browser_parser = subparsers.add_parser("browser", aliases=["b"], help="Open \
            a new tab in a browser and show the result of a search. Usage: \
            tatoeba-karini browser [source_language] [target_language] [term]")
    browser_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    browser_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    browser_parser.add_argument("term", type=str, help="The term \
            to be searched")
    browser_parser.set_defaults(func=browserWrapper)

    download_parser = subparsers.add_parser("download", help="Download \
            files from Tatoeba.org in order to perform off line searches. \
            Download either 'sentences.csv' or 'links.csv'. \
            Usage: tatoeba-karini download [file]")

    download_parser.add_argument("file", type=str, help="The file \
            to be downloaded")
    download_parser.set_defaults(func=downloadWrapper)

    find_parser = subparsers.add_parser("find", aliases=["f"], help="Find \
            sentences containing a term in a specific language. Requires the \
            'sentences.csv' file (reference to the 'download' command). Usage:\
            tatoeba-karini find [target_language] [term]")
    find_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    find_parser.add_argument("term", type=str, help="The term to be searched")
    find_parser.set_defaults(func=findWrapper)

    id_parser = subparsers.add_parser("id", help="Open Tatoeba on the \
            browser searching by sentence's ID. Usage: \
            tatoeba-karini id [target_id]")
    id_parser.add_argument("target_id", type=int, help="The target ID")
    id_parser.set_defaults(func=idWrapper)

    list_languages_parser = subparsers.add_parser("list-languages", help="List \
            languages and their abbreviation used by Tatoeba. Usage: \
            tatoeba-karini list-languages [target_language]")
    list_languages_parser.add_argument("target_language", type=str, help="The \
            abbreviation of the target language name")
    list_languages_parser.set_defaults(func=listAbbreviationWrapper)

    scrap_parser = subparsers.add_parser("scrap", aliases=["s"], help="Scrap \
            data from Tatoeba.org performing a search. \
            Works as the main search on the homepage. Usage: \
            tatoeba-karini scrap [source_language] [target_language] [term]")
    scrap_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    scrap_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    scrap_parser.add_argument("term", type=str, help="The term \
            to be searched")
    scrap_parser.set_defaults(func=requestWrapper)

    translate_parser = subparsers.add_parser("translate", aliases=["t"], help="Search \
            for sentences containing term in a specific language and the \
            translations of the sentence in another language. The local \
            version of the standard search performed on tatoeba.org. \
            Usage: tatoeba-karini translate [source_language] \
            [target_language] [term]")
    translate_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    translate_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    translate_parser.add_argument("term", type=str, help="The term \
            to be searched")
    translate_parser.set_defaults(func=searchWrapper)

    return(vars(parser.parse_args()))


def main():
    """
    Main function.
    Set the argument parser.
    Call the wrapper function accordingly to the argument passed by the user.
    """

    argsDict = parse_arguments()

    if re.search("browserWrapper", str(argsDict["func"])):
        fromLanguage = str(argsDict["source_language"])
        toLanguage = str(argsDict["target_language"])
        term = str(argsDict["term"])

        browserWrapper(fromLanguage, toLanguage, term)

    elif re.search("findWrapper", str(argsDict["func"])):
        inLanguageF = str(argsDict["target_language"])
        termInArgF = str(argsDict["term"])

        findWrapper(inLanguageF, termInArgF)

    elif re.search("downloadWrapper", str(argsDict["func"])):
        downloadFile = str(argsDict["file"])

        downloadWrapper(downloadFile)

    elif re.search("idWrapper", str(argsDict["func"])):
        sentenceId = str(argsDict["target_id"])

        idWrapper(sentenceId)

    elif re.search("listAbbreviationWrapper", str(argsDict["func"])):
        searchPattern = str(argsDict["target_language"])

        listAbbreviationWrapper(searchPattern)

    elif re.search("requestWrapper", str(argsDict["func"])):
        fromLanguage = str(argsDict["source_language"])
        toLanguage = str(argsDict["target_language"])
        term = str(argsDict["term"])

        requestWrapper(fromLanguage, toLanguage, term)

    elif re.search("searchWrapper", str(argsDict["func"])):
        fromLanguage = str(argsDict["source_language"])
        toLanguage = str(argsDict["target_language"])
        term = str(argsDict["term"])
        searchWrapper(fromLanguage, toLanguage, term)

    elif re.search("version", str(argsDict["func"])):
        print(argsDict)

    else:
        print("Ooops!")


# ---------------------------
# call the main

if __name__ == '__main__':
    main()
