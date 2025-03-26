import re

def contains(word, string): return bool(re.search(r'\b' + re.escape(word.lower()) + r'\b', string.lower()))

def rev_dir(string, pairs={'(': ')', '[': ']', '{': '}', '<': '>', ')': '(', ']': '[', '}': '{', '>': '<'}):
    final = ""
    for char in reversed(string):
        if char in pairs:
            final += pairs[char]
        else:
            final += char
    return final