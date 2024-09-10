from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import pickle

# Load the saved TF-IDF Vectorizer and DataFrame
with open('model/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open('model/books_df.pkl', 'rb') as f:
    books = pickle.load(f)

# Combine relevant columns for text-based similarity
books['combined_features'] = books.apply(lambda x: f"{x['Name']} {x['Authors']} {x['Publisher']}", axis=1)
tfidf_matrix = tfidf_vectorizer.transform(books['combined_features'])

def recommend_books(query_params, top_n=5):
    query_parts = []
    if 'name' in query_params:
        query_parts.append(f"Name:{query_params['name']}")
    if 'authors' in query_params:
        query_parts.append(f"Authors:{query_params['authors']}")
    if 'publish_year' in query_params:
        query_parts.append(f"PublishYear:{query_params['publish_year']}")
    if 'publisher' in query_params:
        query_parts.append(f"Publisher:{query_params['publisher']}")

    if not query_parts:
        raise ValueError("At least one search criterion must be provided.")

    query_text = ' '.join(query_parts)
    query_vector = tfidf_vectorizer.transform([query_text])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]
    top_books = books.iloc[top_indices]
    return top_books[['Name', 'Authors', 'PublishYear', 'Publisher', 'Description']].to_dict(orient='records')
