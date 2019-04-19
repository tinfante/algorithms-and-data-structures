#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


def tree():
    return defaultdict(tree)


def make_trie(*words):
    trie = tree()
    for word in words:
        node = trie
        for char in word:
            node = node[char]
        node['end'] = 'end'
    return trie


def has_word(trie, word):
    node = trie
    for char in word:
        if char not in node.keys():
            return False
        node = node[char]
    if node.get('end') == 'end':
        return True
    return False


def has_prefix(trie, prefix):
    """
    Accepts two arguments: a trie and a prefix string. Returns the node for a
    prefix if it exists in trie. Returns False if the prefix isn't in the
    trie (or if it is a word with no suffixes).
    """
    node = trie
    for char in prefix:
        if char not in node.keys():
            return False
        node = node[char]
    if len(node.keys()) == 1 and 'end' in node.keys():
        return False
    return node


def get_suffixes(*args):
    """
    Accepts two arguments: a trie and a prefix string. Returns a list of
    suffixes for that prefix, or an empty list if the prefix doesn't exist
    in the trie.
    """
    if len(args) == 2:
        trie, prefix = args
        prefix_node = has_prefix(trie, prefix)
        if not prefix_node:
            return []
        traversed = ()
        suffixes = []
        return get_suffixes(prefix_node, traversed, suffixes)
    elif len(args) == 3:
        node, traversed, suffixes = args
        for key, child in node.items():
            if key == 'end' and child == 'end':
                if traversed:
                    suffixes.append(''.join(traversed))
            else:
                get_suffixes(child, traversed + (key,), suffixes)
        return suffixes


def suggest(trie, prefix):
    return [prefix+suffix for suffix in get_suffixes(trie, prefix)]
