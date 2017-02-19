# Tatoeba-query

Open tatoeba.org from the command line.

## Requirements 

Probably Python 3.\*. So far, it has been used only on Linux with Python 3.6.

## Requirements for offline searches

If you want to make use of the `-f` command (to perform offline searches), make
sure have the file containing the sentences:
[sentences.csv](http://downloads.tatoeba.org/exports/sentences.tar.bz2).

The file should be: 
- downloaded (yes, that's right, more than 80MB, about 5511497 lines of pure joy)
- decompressed (`$ tar -xvfj sentences.csv`)
- be sure it is placed on the root of the Tatoeba-query directory

## Usage 

```
python tatoeba-query [OPTION] [OPTION'S ARGUMENTS]
```

| Optional command | Description | Arguments needed | Syntax | Example |
|------------------|-------------|------------------|--------|---------|
| -b               | Open the browser in a new tab performing a search on tatoeba.org | 3 | tatoeba-query -b [FROM-LANGUAGE] [TO-LANGUAGE] | `$ tatoeba-query -b eng jpn breath` |
| -f               | Find sentences in X language containing the Y-term | 2 | tatoeba-query -f [IN-LANGUAGE] [TERM] | `$ tatoeba-query -f yor water` |


## TODO list

- [X] Open Tatoeba.org from the command line
- [ ] Query even if [offline](https://tatoeba.org/eng/downloads)
- [ ] Create a command to list all language's abbreviations used by Tatoeba
- [ ] Fetch data back to the shell (in instead of opening the browser)
- [ ] Create a Vim/Neovim plugin and enjoy it o/

## License

All the creative content is licensed by [Tatoeba.org](https://tatoeba.org)under CC-BY 2.0.

Tatoeba-query is a _personal_ project, which aims to provide a faster way to
check the amazing resource of Tatoeba.org from the command line. I'm working on
it **as** and **while** learning to program independently. By no means it should
be used for something serious.

## Issues, bugs, contributions

If you have any problem while using Tatoeba-query, **please**:

- do **not** bother the Tatoeba's team. They are already doing an amazing work
  out there. (:
- And create issue here. Any feedback is a good feedback. (:
