from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load and clean the dataset
newsgroups_data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
documents = newsgroups_data.data
documents = [doc for doc in documents if len(doc.strip()) > 50]

# Step 2: Vectorize the documents
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_matrix = vectorizer.fit_transform(documents)

# Step 3: Define the search function
def search_documents(query, top_n=5):
    if not query.strip():
        return []
    
    query_vec = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    
    results = []
    for idx in top_indices:
        snippet = documents[idx][:300].replace('\n', ' ').strip()
        results.append((snippet, similarity_scores[idx]))
    
    return results
