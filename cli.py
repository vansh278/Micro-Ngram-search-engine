from indexer import InMemoryIndexer
from document import Document

def main():
    idx = InMemoryIndexer()
    print("Enter documents (type 'done' when finished):")
    i = 1
    while True:
        content = input(f"Doc {i}: ")
        if content.lower() == "done":
            break
        idx.add_document(Document(str(i), content))
        i += 1

    while True:
        query = input("Query> ")
        if query.lower() in ("exit", "quit"):
            break
        results = idx.search(query)
        print("Results:", results)

if __name__ == "__main__":
    main()
