from flask import Flask, render_template, request
from search_engine.search import SearchEngine

app = Flask(__name__)

engine = SearchEngine()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = engine.search(query) if query else []
    return render_template("results.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
