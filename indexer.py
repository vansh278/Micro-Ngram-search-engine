import math, json, hashlib
from tokenizer import tokenize

class InMemoryIndexer:
    def __init__(self):
        self.inverted_index = {}
        self.doc_lengths = {}
        self.total_docs = 0

    def _hash_key(self, token):
        return hashlib.sha256(token.encode()).hexdigest()[:8]

    def add_document(self, doc):
        self.total_docs += 1
        tokens = tokenize(doc.content)
        self.doc_lengths[doc.doc_id] = len(tokens)

        for pos, token in enumerate(tokens):
            key = self._hash_key(token)
            if key not in self.inverted_index:
                self.inverted_index[key] = {}
            if doc.doc_id not in self.inverted_index[key]:
                self.inverted_index[key][doc.doc_id] = []
            self.inverted_index[key][doc.doc_id].append(pos)

    def search(self, query):
        tokens = tokenize(query)
        doc_scores = {}
        for token in tokens:
            key = self._hash_key(token)
            postings = self.inverted_index.get(key, {})
            df = len(postings)
            idf = math.log((self.total_docs + 1) / (df + 1)) + 1

            for doc_id, positions in postings.items():
                tf = len(positions)
                tf_weight = tf / self.doc_lengths[doc_id]
                score = idf * tf_weight
                doc_scores[doc_id] = doc_scores.get(doc_id, 0) + score

        return dict(sorted(doc_scores.items(), key=lambda item: item[1], reverse=True))

