# Tatoeba-query

Open tatoeba.org from the command line.

## Requirements

Python 3.*

## Usage 

```
python tatoeba-query [COMMAND] [from-language] [to-language] [term]

Look for sentences in french containing the french word equivalent to the english word 'water':

```
python tatoeba-query browser eng fra water
```

The only command implemented so far is "browser" to open the browser in a new
tab (if possible). 

## TODO list

- Fetch data back to the shell (in instead of opening the browser)
- Create a command to list all language's abbreviations used by Tatoeba
- Create a Vim/Neovim plugin and enjoy it o/
