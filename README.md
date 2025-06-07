# 🧠 AI Text Search Engine

This project is a simple AI-powered search engine built using Python, Flask, and TF-IDF.  
It allows users to search through a large set of documents from the [20 Newsgroups dataset](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html) and returns the most relevant text snippets based on the input query.

---

## 📌 Features

- Keyword-based search using TF-IDF
- Cosine similarity ranking
- Web interface with Flask
- Responsive layout with basic CSS
- Tested locally and ready for deployment

---

## 🧰 Technologies Used

- Python 3
- Flask
- scikit-learn
- TF-IDF (for document vectorization)
- Cosine similarity (for ranking results)
- HTML, CSS (basic styling)

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-search-engine.git
   cd ai-search-engine

2. **Create and activate a virtual environment**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the app**
    python app.py

5. **Open your browser**
    Go to http://127.0.0.1:5000 to use the search engine.

---

## 📂 Project Structure

````markdown
STAI project/
├── app.py                  # Flask app
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── utils/
│   ├── search_engine.py    # TF-IDF logic and search function
│   └── __init__.py
├── static/
│   └── style.css           # CSS styles
├── templates/
│   ├── search.html         # Search form
│   └── results.html        # Search results


---

## 🧠 What This Demonstrates

Classic NLP: TF-IDF and cosine similarity
Full-stack AI project: From backend logic to frontend UI
How simple AI techniques can power useful real-world applications

---

## 🧩 Future Improvements

Semantic search with Sentence Transformers
Filter results by category
Paginate results or show full document
Host online (e.g., with Render, Heroku)