from flask import Flask, request, jsonify
from indexer import InMemoryIndexer
from document import Document

app = Flask(__name__)
indexer = InMemoryIndexer()

@app.route("/add", methods=["POST"])
def add_doc():
    data = request.json
    doc = Document(data["id"], data["content"])
    indexer.add_document(doc)
    return jsonify({"status": "success"})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    results = indexer.search(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
