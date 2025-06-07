import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import search_engine

print("Total documents:", len(search_engine.documents))
print("\nTop results for query: 'space mission'\n")

results = search_engine.search_documents("space mission", top_n=3)
for i, (text, score) in enumerate(results, 1):
    print(f"Result {i} (Score: {score:.4f}):\n{text}\n{'-'*40}")
