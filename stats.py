import math

class IndexStats:
    def __init__(self):
        self.doc_count = 0
        self.df = {}

    def update(self, term, doc_id):
        self.df.setdefault(term, set()).add(doc_id)
        self.doc_count += 1

    def idf(self, term):
        df = len(self.df.get(term, []))
        if df == 0:
            return 0
        return math.log(self.doc_count / df)
