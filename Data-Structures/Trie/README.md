# Trie

A tree-like structure where nodes are characters, and child nodes are characters that follow that character in the strings loaded into the data structure.

## Python

Quick and simple implementation of a Trie in Python, along with functions to check if a word or prefix exists, and to get the possible suffixes for a prefix (which allows offering auto-complete suggestions). Needless to say, a nested dictionary approach isn't efficient and won't scale well, so it's better a use a library. Furthermore, for a lot of data a better option might be a [DAFSA or DAWG](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton).

## Clojure

See [word-autocomplete](https://github.com/tinfante/word-autocomplete).


##### References

* [Wikipedia article](https://en.wikipedia.org/wiki/Trie).
