from flask import Flask, request, render_template
from utils import search_engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_engine.search_documents(query, top_n=5)
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
