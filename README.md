# Tatoeba-karini

Consult tatoeba.org from the command line.

WARNING: this project is **extremely experimental**. (:

## Requirements 

Probably Python 3.\*. So far, it has been used only on Linux with Python 3.6.

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

| Optional command | Description | Required arguments | Syntax | Example |
|------------------|-------------|------------------|--------|---------|
| -b               | Open the browser in a new tab performing a search on tatoeba.org | 3 | -b [FROM-LANGUAGE] [TO-LANGUAGE] | `$ tatoeba-karini -b eng jpn breath` |
| -f               | Find sentences in X language containing the Y-term | 2 | -f [IN-LANGUAGE] [TERM] | `$ tatoeba-karini -f yor water` |
| -l               | List languages and their abbreviation used by Tatoeba | 1 | -l [LANGUAGE-NAME] | `$ tatoeba-karini -l Japanese` |
| -r               | Request from Tatoeba.org. Works in the same way as the main
search on the website | 3 | -r [FROM-LANGUAGE] [TO-LANGUAGE] [TERM] | `$
tatoeba-karini -r eng ara watermelon` |
| -s               | Search for sentences containing term in a specific language and it the counterparts of the sentence in another language | 3 | -s [IN-LANGUAGE] [TO-LANGUAGE] [TERM] | `$ tatoeba-karini -s eng jpn air` |
| -i               | Open Tatoeba on the browser searching by sentence's ID | 1 | -i [SENTENCE'S-ID] | `$ tatoeba-karini -i 825762` |


## TODO list

- [x] Open Tatoeba.org from the command line
- [x] Query even if [offline](https://tatoeba.org/eng/downloads)
- [x] Create a command to list all language's abbreviations used by Tatoeba
- [x] Search Tatoeba.org by sentence's ID
- [ ] Fetch data back to the shell (in instead of opening the browser)
- [ ] Create a Vim/Neovim plugin and enjoy it o/
- [ ] Download and uncompress files as needed
- [ ] Improve performance, clean the code of everything

## License

All the creative content is licensed by [Tatoeba.org](https://tatoeba.org)under CC-BY 2.0.

Tatoeba-karini is a _personal_ project, which aims to provide a faster way to
check the amazing resource of Tatoeba.org from the command line. I'm working on
it **as** and **while** learning to program independently. By no means it should
be used for something serious.

## Issues, bugs, contributions

If you have any problem while using Tatoeba-karini, **please**:

- do **not** bother the Tatoeba's team. They are already doing an amazing work
  out there. (:
- And create issue here. Any feedback is a good feedback. (:
