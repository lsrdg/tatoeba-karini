"""
Tatoeba-karini      | tatoeba.org from the command line
---

Run it with the '--help' option for more information.
"""
import webbrowser
import argparse
import os
import csv
import re
import tarfile
import requests
import bs4


# --------------------------
# find and store real path

REAL_PATH = os.path.dirname(os.path.realpath(__file__))

# --------------------------
# Functions for the main LOCAL search

# The main search stuff

SENTENCES = []
TRANSLATIONS_LIST = []


def find_translation(register, in_language_s, to_language_s, pattern_in_arg_s):
    """
    Make use of the file `links.csv` to check if a sentence has a translation
    in the target language specified by the user.
    """

    with open(REAL_PATH + '/links.csv') as links:
        links_list = csv.reader(links, delimiter='\t')

        for line in links_list:
            if line[0] == register:
                test_check_id = line[1]
                check_translation(
                    test_check_id, in_language_s, to_language_s, pattern_in_arg_s)
                continue
            else:
                pass


def check_translation(possible_id, in_language_s, to_language_s, pattern_in_arg_s):
    """
    Check on the file `sentences.csv` if a translation exists. If it does, it
    will be printed, or else, move on to the next iteration.
    """

    with open(REAL_PATH + '/sentences.csv') as sentences_listing:
        sentences_list = csv.reader(sentences_listing, delimiter='\t')
        for row in sentences_list:
            if row[0] == possible_id and to_language_s == row[1]:
                TRANSLATIONS_LIST.append(row)
                print(SENTENCES[-1])
                print(TRANSLATIONS_LIST[-1], '\n\n')
                continue
            else:
                pass


def find_translated_pattern(in_language_s, to_language_s, pattern_in_arg_s):
    """
    Takes the user input and checks if there is a sentence containing the
    searched pattern in the desired source language.

    If there is, move on and call `find_translation()` to find possible
    translations. If not, pass.
    """

    with open(REAL_PATH + '/sentences.csv') as sentences_listing:
        sentences_list = csv.reader(sentences_listing, delimiter='\t')

        for row in sentences_list:
            if row[1] == in_language_s and pattern_in_arg_s in row[2]:
                SENTENCES.append(row)
                find_translation(row[0], in_language_s, to_language_s, pattern_in_arg_s)

            elif row[1] != in_language_s or pattern_in_arg_s not in row[2]:
                pass
# Define argument function


def browser_wrapper(source_lang, target_lang, pattern):
    """
    Wrapper to the 'browser' functionality.
    Open tatoeba.org in a new tab browser performing a search
    """

    # ArgB variables
    from_reference = '&from='
    to_reference = '&to='

    # Join everything to perform the search
    search = pattern + from_reference + source_lang + to_reference + target_lang

    # Open the browser
    webbrowser.open(
        'https://tatoeba.org/eng/sentences/search?query=' + search, new=2
    )


def download_wrapper(download_file):
    """
    Wrapper for the download functionality.
    Download and uncompress the files needed by the off line search/find
    functionalities.
    """

    def download_tool():
        """
        Download the `sentences.csv` file or the `links.csv` file.
        """

        with open(REAL_PATH + download_file + '.tar.bz2', 'wb') as the_file:
            print('Downloading the ',
                  download_file, 'file, in the \'.tar.bz2\' format.')
            print('Please wait.')
            res = requests.get('http://downloads.tatoeba.org/exports/' +
                               download_file + '.tar.bz2')
            res.raise_for_status()
            if not res.ok:
                print('Download failed.')

            for block in res.iter_content(1024):
                the_file.write(block)

            print('Download finished.\n\n')

    def uncompress_tool():
        """
        Uncompress the downloaded file.
        """

        print('\n\nUncompressing the', download_file, 'file. Please wait.')
        untar_file = tarfile.open(REAL_PATH + download_file + '.tar.bz2', 'r:bz2')
        untar_file.extractall(REAL_PATH)
        untar_file.close()
        print('File uncompressed and ready to use.\n')

    if download_file == 'sentences' or download_file == 'links':
        pass
    elif download_file != 'sentences' or download_file != 'links':
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

    ask_for_download = input('> ')

    if ask_for_download.lower() == 'yes' or ask_for_download.lower() == 'y':
        download_tool()
        uncompress_tool()

    else:
        print("""
                \n\nNo problems. You can always download and
                extract the files manually.
                Just head to https://tatoeba.org/eng/downloads.
                \n
              """)


def id_wrapper(sentence_id):
    """
    Open Tatoeba.org in a new tab searching by sentence's ID, just in case.
    Use it to get more information about the sentence.
    """
    webbrowser.open(
        'https://tatoeba.org/eng/sentences/show/' + sentence_id, new=2
    )


def find_wrapper(target_lang, pattern):
    """
    Wrapper for the `find` functionality.
    Make use of the 'sentences.csv' file to to find a sentence containing
    a pattern in an language.
    """

    # find_wrapper variables
    with open(REAL_PATH + '/sentences.csv') as list_file:
        read_list = csv.reader(list_file, delimiter='\t')

        def find_pattern_in_target_lang():
            """
            function responsible for making the search AND looping the matches.
            """
            found_pattern = [
                row
                for row in read_list
                if row[1] == target_lang and pattern in row[2]
            ]

            for row in found_pattern:
                print(row)

        find_pattern_in_target_lang()



def list_abbreviation_wrapper(search_pattern):
    """
    Look for the abbreviation of language.
    Necessary for the off line searches.
    The abbreviations follow Tatoeba's pattern.
    """

    with open(REAL_PATH + '/abbreviation_list.csv') as abbreviation_list:
        search_pattern = search_pattern.lower()
        abbrev_list = csv.reader(abbreviation_list, delimiter='\t')
        abbreviation = [
            row for row in abbrev_list if search_pattern in map(
                str.lower, row)
            ]
        print(abbreviation)


# Fetching
def request_get(search):
    """
    Returns an object of the get method of requests.
    """

    res = requests.get(search)
    return res


def request_pagination_input(value):
    """
    Return whether the user want to see the next page or not.
    """
    user_input = input(value)
    if user_input == "y":
        return user_input
    elif user_input == "n":
        return user_input
    else:
        return print('Invalid input.')


def request_pagination(search):
    """
    Simulate `request_wrapper()`'s behavior in case the user wants to
    paginate the results.
    """
    res = request_get(search)
    to_print = request_print(res)
    return to_print


def request_print(value):
    """
    Wrapper the 'printing' aspects of `request_wrapper()`.
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
            return False
        else:
            print("\n".join("{}".format(el.find(
                'div', class_='text').get_text()) for el in elements), '\n')
            pagination_href = pagination.find('a', href=True)
            return pagination_href.get('href')

    except AttributeError:
        pass


def request_wrapper(source_lang, target_lang, pattern):
    """
    Wrapper for the 'request' functionality.
    Scrap tatoeba.org.

    Support basic forward pagination.
    """

    url_base = 'https://tatoeba.org'
    search_base = '/eng/sentences/search?'
    from_reference = 'from='
    to_reference = '&to='
    query = '&query='

    # Join everything to perform the search

    search = url_base + search_base + from_reference + source_lang +\
        to_reference + target_lang + query + pattern
    res = request_get(search)

    pagination = request_print(res)

    while pagination is not False:
        next_page = request_pagination_input('Next page? (y/n) ')
        if next_page == "n":
            return print('Ok, no pagination this time...')
        elif next_page == "y":
            search = url_base + pagination
            pagination = request_pagination(search)
    else:
        return


def translate_wrapper(in_language_s, to_language_s, pattern_in_arg_s):
    """
    Wrapper for the search functionality, which despite
    of its complexity, is implemented with the use of the
    'find' functionality.
    """

    find_translated_pattern(in_language_s, to_language_s, pattern_in_arg_s)

# --------------------------
# Define command line menu function


def parse_arguments():
    """
    Parse and return arguments.
    """

    parser = argparse.ArgumentParser("tatoeba-karini [COMMAND] [ARGUMENT(S)]")

    parser.add_argument("--version", "-v", action="version", version="v0.0.6+")

    subparsers = parser.add_subparsers(help="Types of commands")

    browser_parser = subparsers.add_parser("browser", aliases=["b"], help="Open \
            a new tab in a browser and show the result of a search. Usage: \
            tatoeba-karini browser [source_language] [target_language] [term]")
    browser_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    browser_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    browser_parser.add_argument("pattern", type=str, help="The pattern \
            to be searched")
    browser_parser.set_defaults(func=browser_wrapper)

    download_parser = subparsers.add_parser("download", help="Download \
            files from Tatoeba.org in order to perform off line searches. \
            Download either 'sentences.csv' or 'links.csv'. \
            Usage: tatoeba-karini download [file]")

    download_parser.add_argument("file", type=str, help="The file \
            to be downloaded")
    download_parser.set_defaults(func=download_wrapper)

    find_parser = subparsers.add_parser("find", aliases=["f"], help="Find \
            sentences containing a pattern in a specific language. Requires the \
            'sentences.csv' file (reference to the 'download' command). Usage:\
            tatoeba-karini find [target_language] [term]")
    find_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    find_parser.add_argument("pattern", type=str, help="The pattern to be searched")
    find_parser.set_defaults(func=find_wrapper)

    id_parser = subparsers.add_parser("id", help="Open Tatoeba on the \
            browser searching by sentence's ID. Usage: \
            tatoeba-karini id [target_id]")
    id_parser.add_argument("target_id", type=int, help="The target ID")
    id_parser.set_defaults(func=id_wrapper)

    abbreviate_parser = subparsers.add_parser("abbreviate", aliases=["ab"], \
            help="List languages and their abbreviation used by Tatoeba. \
            Usage: tatoeba-karini abbreviate [target_language]")
    abbreviate_parser.add_argument("target_language", type=str, help="The \
            abbreviation of the target language name")
    abbreviate_parser.set_defaults(func=list_abbreviation_wrapper)

    scrap_parser = subparsers.add_parser("scrap", aliases=["s"], help="Scrap \
            data from Tatoeba.org performing a search. \
            Works as the main search on the homepage. Usage: \
            tatoeba-karini scrap [source_language] [target_language] [term]")
    scrap_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    scrap_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    scrap_parser.add_argument("pattern", type=str, help="The pattern \
            to be searched")
    scrap_parser.set_defaults(func=request_wrapper)

    translate_parser = subparsers.add_parser("translate", aliases=["t"], help="Search \
            for sentences containing pattern in a specific language and the \
            translations of the sentence in another language. The local \
            version of the standard search performed on tatoeba.org. \
            Usage: tatoeba-karini translate [source_language] \
            [target_language] [term]")
    translate_parser.add_argument("source_language", type=str, help="A three \
            characters abbreviation of the source language")
    translate_parser.add_argument("target_language", type=str, help="A three \
            characters abbreviation of the target language")
    translate_parser.add_argument("pattern", type=str, help="The pattern \
            to be searched")
    translate_parser.set_defaults(func=translate_wrapper)

    return vars(parser.parse_args())


def main():
    """
    Main function.
    Set the argument parser.
    Call the wrapper function accordingly to the argument passed by the user.
    """

    args_dict = parse_arguments()

    if re.search("browser_wrapper", str(args_dict["func"])):
        source_lang = str(args_dict["source_language"])
        target_lang = str(args_dict["target_language"])
        pattern = str(args_dict["pattern"])

        browser_wrapper(source_lang, target_lang, pattern)

    elif re.search("find_wrapper", str(args_dict["func"])):
        target_lang = str(args_dict["target_language"])
        pattern = str(args_dict["pattern"])

        find_wrapper(target_lang, pattern)

    elif re.search("download_wrapper", str(args_dict["func"])):
        download_file = str(args_dict["file"])

        download_wrapper(download_file)

    elif re.search("id_wrapper", str(args_dict["func"])):
        sentence_id = str(args_dict["target_id"])

        id_wrapper(sentence_id)

    elif re.search("list_abbreviation_wrapper", str(args_dict["func"])):
        search_pattern = str(args_dict["target_language"])

        list_abbreviation_wrapper(search_pattern)

    elif re.search("request_wrapper", str(args_dict["func"])):
        source_lang = str(args_dict["source_language"])
        target_lang = str(args_dict["target_language"])
        pattern = str(args_dict["pattern"])

        request_wrapper(source_lang, target_lang, pattern)

    elif re.search("translate_wrapper", str(args_dict["func"])):
        source_lang = str(args_dict["source_language"])
        target_lang = str(args_dict["target_language"])
        pattern = str(args_dict["pattern"])
        translate_wrapper(source_lang, target_lang, pattern)

    elif re.search("version", str(args_dict["func"])):
        print(args_dict)

    else:
        print("Ooops!")


# ---------------------------
# call the main

if __name__ == '__main__':
    main()
