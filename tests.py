from indexer import InMemoryIndexer
from document import Document

def test_index_and_search():
    idx = InMemoryIndexer()
    idx.add_document(Document("1", "Hello world"))
    idx.add_document(Document("2", "Hello there"))
    result = idx.search("Hello")
    assert "1" in result and "2" in result

def test_search_multiple_terms():
    idx = InMemoryIndexer()
    idx.add_document(Document("1", "quick brown fox"))
    idx.add_document(Document("2", "quick blue hedgehog"))
    result = idx.search("quick brown")
    assert list(result.keys())[0] == "1"
