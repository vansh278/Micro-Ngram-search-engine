import re

STOPWORDS = {"the", "is", "at", "which", "on", "and", "a"}

def edge_ngrams(word, min_len=2, max_len=5):
    return [word[:i] for i in range(min_len, min(len(word), max_len) + 1)]

def tokenize(text):
    words = re.findall(r'\b\w+\b', text.lower())
    tokens = []
    for word in words:
        if word not in STOPWORDS:
            tokens.extend(edge_ngrams(word))
    return tokens

