# Tatoeba-karini

[![Build
Status](https://travis-ci.org/lsrdg/tatoeba-karini.svg?branch=master)](https://travis-ci.org/lsrdg/tatoeba-karini)

tatoeba.org from the command line.

Tatoeba-karini can assist you on opening and scrapping tatoeba.org from the
terminal, find sentences and translations without internet connection and some
commands to help on the general usage of the script (e.g. downloading and uncompressing
needed files).

The project is currently on
**[v0.0.5](https://github.com/lsrdg/tatoeba-karini/releases/tag/v0.0.5)**.

WARNING: this project is **extremely experimental**. Come together! (:

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
I was missing was access to the great material available on Tatoeba, not any more.

And in order to learn Python and programming, I needed a project that I do care 
about.

## Roadmap

You can follow the [milestones of the
project](https://github.com/lsrdg/tatoeba-karini/milestones).

**Short term**: until `v0.1`, the focus will be on improving what already
exists, both terms of code and user experience.

**Long term**: improve what already exists and add more functionality 

- to be an alternative to offline use of Tatoeba
- export data (`.csv` files, e.g. to be used on [Anki](https://apps.ankiweb.net/))
- strong REGEX parser
- more ways to interact with Tatoeba and all the material provided by it

## Requirements 

Python 3.\*. It was written on Arch Linux with Python 3.6.
Theoretically, it should work on any system with support to Python 3.

For a complete list, please take a look at
[`requirements.txt`](requirements.txt).

If you care, please open an issue sharing how was your experience on your
environment.

### Requirements for offline searches

If you want to make use of the `find` command (to perform offline searches), make
sure have the file containing the sentences:
[sentences.csv](http://downloads.tatoeba.org/exports/sentences.tar.bz2).

The `translate` command makes use of the `sentences.csv` mentioned above *and* [links.csv](http://downloads.tatoeba.org/exports/links.tar.bz2).

The files should be: 
- downloaded (yes, that's right, more than 80MB, about 5511497 lines of pure joy)
- decompressed (`$ tar -xvfj sentences.csv`)
- be sure it is placed on the root of the Tatoeba-karini directory

**Heads up!** The `download` command can... erh, download and prepare the file for you.

## Usage 

```
python tatoeba-karini [COMMAND] [ARGUMENT(S)]
```

The script can perform different actions, such as:

- Open tatoeba.org on the browser
- Scrap tatoeba.org performing a search
- Search off line making use of the [sentences' file](https://tatoeba.org/eng/downloads)


| Positional command | Description                                                                                                             | Required arguments | Example                                  |
|------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------|
| `browser` (or `b`)               | Open the browser in a new tab performing a search on tatoeba.org                                                        | 3 | `$ tatoeba-karini -b eng jpn breath`     | 
| `find` (or `f`)               | Find sentences in X language containing the Y-term                                                                      | 2 |  `$ tatoeba-karini find yor water`          |
| `list-languages`               | List languages and their abbreviation used by Tatoeba                                                                   | 1 |  `$ tatoeba-karini list-languages Japanese`           |
| `scrap` (or `s`               | Scrap Tatoeba.org. Works in the same way as the main search on the website                                       | 3 |  `$ tatoeba-karini scrap eng ara watermelon` |
| `translate` (or `t`)               | Search for sentences containing term in a specific language and the translation of the sentences in another language | 3 | `$ tatoeba-karini translate eng jpn air`        |
| `id`               | Open Tatoeba on the browser searching by sentence's ID | 1                  | `$ tatoeba-karini id 825762`             |
| `download`               | Download files (`links` or `sentences`) from Tatoeba.org in order to perform offline searches                            | 1 | `$ tatoeba-karini download links`              |
| `--version` (or `-v`) | Prints the version | 0 | `$ tatoeba-karini --version`

> Need help? `$ tatoeba-karini --help` will show a list of the commands, what
> they do and tell you what you need to make them work.

### Notes

About the commands and their current state:

- There are two commands for **opening** Tatoeba.org from the command line
  (`browser`, `id`), and they _should_ just work. There are also other commands
  that might get their own 'open in the browser' version on the future.

- All the offline commands need improvement. `find` is working pretty well for my
  personal use, but still need some REGEX to work as it should. `translate` is the worst 
  of all of them, taking several minutes to perform even the most basic search.
  The inefficiency of these commands reflect how much I need to learn, any help
  welcome. (:

- The fetching/scrapping command `scrap` is not perfect, but it is what I had in
  mind before this project got started. A better support for multiple pages is planned.
  
## License

All the creative content is licensed by [Tatoeba.org](https://tatoeba.org) under
CC-BY 2.0. For more information on the Tatoeba project, please head to
tatoeba.org .

Tatoeba-karini is released under [GNU
AGPLv3](https://choosealicense.com/licenses/agpl-3.0/#). A copy of the license
is available [here](LICENSE.txt).

## Issues, bugs, contributions

If you have any problem while using Tatoeba-karini, **please**:

- do **not** bother the Tatoeba's team. They are already doing an amazing work
  out there. (:
- And create an issue here. Any feedback is a good feedback. (:
- being the only user, I have no idea how it behaves over there, let me know if
  you don't mind.

The project is being maintained on Github:
https://github.com/lsrdg/tatoeba-karini

However, there is a mirror of it on Gitlab:
https://gitlab.com/lsrdg/tatoeba-karini

The repository on Gitlab is to anyone who doesn't want to bother
with Github to have an alternative to report issue. Keep mind that (at least for
now) everything will be redirected to Github.

## Thank you!

Special thanks to the team of Tatoeba.org for keeping this amazing project
alive!

Another special thanks goes to @Spindel for the guidance and great suggestions.

In a matter of fact, thanks to those who cared to open an issue, star and/or
fork.
That's great to be aware of other people looking for this kind of stuff. (:
