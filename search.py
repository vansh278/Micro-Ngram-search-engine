from indexer import InMemoryIndexer
from document import Document

class SearchEngine:
    def __init__(self):
        self.indexer = InMemoryIndexer()

    def index_document(self, doc_id, content, metadata=None):
        doc = Document(doc_id, content, metadata)
        self.indexer.add_document(doc)

    def search(self, query):
        return self.indexer.search(query)
