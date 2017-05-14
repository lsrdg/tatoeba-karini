# Tatoeba-karini

Consult tatoeba.org from the command line.

WARNING: this project is **extremely experimental**. (:

> Tatoeba.org is a free collaborative online database of example sentences geared
> towards foreign language learners. Its name comes from the Japanese term
> "tatoeba" (例えば　_tatoeba_), meaning "for example". Unlike other online
> dictionaries, which focus on words, **Tatoeba** focuses on translation of complete
> sentences. In addition, the structure of the database and interface emphasize
> one-to-many relationships. Not only can a sentence have multiple translations
> within a single language, but its translations into all languages are readily
> visible, as are indirect translations that involve a chain of stepwise links
> from one language to another.

_from [Wikipedia](https://en.wikipedia.org/wiki/Tatoeba)_ 

## Why?/Motivation

If you work on the command line and deal with language stuff, you probably make
use of some editor, dictionary, translator, thesaurus etc. The only thing 
missing was access to the great material available on Tatoeba, not any more.

## Requirements 

Probably Python 3.\*. So far, it has been used only on Archlinux with Python 3.6.

### Requirements for offline searches

If you want to make use of the `-f` command (to perform offline searches), make
sure have the file containing the sentences:
[sentences.csv](http://downloads.tatoeba.org/exports/sentences.tar.bz2).

The command `-s` makes use of the `sentences.csv` *and*:
[links.csv](http://downloads.tatoeba.org/exports/links.tar.bz2).

The files should be: 
- downloaded (yes, that's right, more than 80MB, about 5511497 lines of pure joy)
- decompressed (`$ tar -xvfj sentences.csv`)
- be sure it is placed on the root of the Tatoeba-karini directory

## Usage 

```
python tatoeba-karini [OPTION] [OPTION'S ARGUMENTS]
```

| Optional command | Description                                                                                                             | Required arguments | Syntax                                  | Example                                  |
|------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------|------------------------------------------|
| -b               | Open the browser in a new tab performing a search on tatoeba.org                                                        | 3                  | -b [FROM-LANGUAGE] [TO-LANGUAGE]        | `$ tatoeba-karini -b eng jpn breath`     |
| -f               | Find sentences in X language containing the Y-term                                                                      | 2                  | -f [IN-LANGUAGE] [TERM]                 | `$ tatoeba-karini -f yor water`          |
| -l               | List languages and their abbreviation used by Tatoeba                                                                   | 1                  | -l [LANGUAGE-NAME]                      | `$ tatoeba-karini -l Japanese`           |
| -r               | Request from Tatoeba.org. Works in the same way as the main search on the website                                       | 3                  | -r [FROM-LANGUAGE] [TO-LANGUAGE] [TERM] | `$ tatoeba-karini -r eng ara watermelon` |
| -s               | Search for sentences containing term in a specific language and it the counterparts of the sentence in another language | 3                  | -s [IN-LANGUAGE] [TO-LANGUAGE] [TERM]   | `$ tatoeba-karini -s eng jpn air`        |
| -i               | Open Tatoeba on the browser searching by sentence's ID                                                                  | 1                  | -i [SENTENCE'S-ID]                      | `$ tatoeba-karini -i 825762`             |
| -d               | Download files (`links` or `sentences`) from Tatoeba.org in order to perform offline searchs                            | 1                  | -d [FILE]                               | `$ tatoeba-karini -d links`              |


## TODO list

- [x] Open Tatoeba.org from the command line
- [x] Query even if [offline](https://tatoeba.org/eng/downloads)
- [x] Create a command to list all language's abbreviations used by Tatoeba
- [x] Search Tatoeba.org by sentence's ID
- [x] Fetch data back to the shell (in instead of opening the browser)
- [ ] Create a Vim/Neovim plugin and enjoy it o/
- [x] Download and uncompress files as needed
- [ ] Improve performance, clean the code of everything

### Notes

About the commands and their current state:

- 2 two commands for **opening** Tatoeba.org from the command line (`-b`,
  `-i`), and they _should_ just work. There are also other commands that should
  get their own 'open in the browser' version.

- All the offline commands need improvement. `-f` is working pretty well for my
  personal use, but still need some REGEX to work as it should. `-s` is worst of
  all of them, taking several minutes to perform even the most basic search. The
  uneficiency of these commands reflect how much I need to learn, any help
  welcome. (:

- The fetching/scrapping command `-r` is not perfect, but it is what I had in
  mind before this project got started. Support for multiple pages and REGEX
  planned.

- Before falling in the rabbit hole of Vimscripting, the plan is to first
  improve the python's performance. That said, in the meanwhile, Tatoeba-karini
  works great _for me_ with the Neovim terminal, being already a great part of
  my writing/studying/working workflow. o/

- All these notes and this bizarre documentation of something that probably
  noone else is gonna use might be senseless, but who knows... o_O
  
## License

All the creative content is licensed by [Tatoeba.org](https://tatoeba.org) under CC-BY 2.0.

Tatoeba-karini is a _personal_ project, which aims to provide a faster way to
check the amazing resource of Tatoeba.org from the command line. I'm working on
it **as** and **while** learning to program independently. By no means it should
be used for something serious.

## Issues, bugs, contributions

If you have any problem while using Tatoeba-karini, **please**:

- do **not** bother the Tatoeba's team. They are already doing an amazing work
  out there. (:
- And create issue here. Any feedback is a good feedback. (:
- being the only user, I have no idea how it behaves over there, let me know if
  you don't mind.
