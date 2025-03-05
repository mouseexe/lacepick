import re

def contains(word, string): return bool(re.search(r'\b' + re.escape(word.lower()) + r'\b', string.lower()))