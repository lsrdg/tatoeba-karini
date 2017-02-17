# Tatoeba-query

Open tatoeba.org from the command line.

## Requirements

Python 3.*

## Usage 

```
python tatoeba-query [COMMAND] [from-language] [to-language] [term]
```

Look for sentences in french containing the french word equivalent to the english word 'water':

```
python tatoeba-query b eng fra water
```

The only command implemented so far is `b` ("b" = "browser") to open the browser in a new
tab (if possible). 

## TODO list

- [X] Open Tatoeba.org from the command line
- [ ] Fetch data back to the shell (in instead of opening the browser)
- [ ] Create a command to list all language's abbreviations used by Tatoeba
- [ ] Query even if [offline](https://tatoeba.org/eng/downloads)
- [ ] Create a Vim/Neovim plugin and enjoy it o/

## License

Tatoeba-query is shared under Creative Commons Attribution 2.0, the same as
[Tatoeba.org](https://tatoeba.org).

Tatoeba-query is a _personal_ project, which aims to provide a faster way to
check the amazing resource of Tatoeba.org from the command line. I'm working on
it **as** and **while** learning to program independently. By no means it should
be used for something serious.

## Issues, bugs, contributions

If you have any problem while using Tatoeba-query, **please**:

- do **not** bother the Tatoeba's team. They are already doing an amazing work
  out there. (:
- And create issue here. Any feedback is a good feedback. (:
