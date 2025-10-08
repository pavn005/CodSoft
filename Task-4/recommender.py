import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


movies = pd.read_csv('movies.csv')  

movies['genres'] = movies['genres'].str.replace('|', ' ')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

nn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)  
nn.fit(tfidf_matrix)

def recommend(title, nn=nn, tfidf_matrix=tfidf_matrix):
    idx = movies[movies['title'].str.lower() == title.lower()].index
    if len(idx) == 0:
        return ["Movie not found."]
    idx = idx[0]
    
    distances, indices = nn.kneighbors(tfidf_matrix[idx])
    
    rec_indices = indices[0][1:]
    return movies['title'].iloc[rec_indices].tolist()

movie = input("Enter Movie Name: ")
print(f"\nRecommended Movies for '{movie}':")
print(recommend(movie.lower()))
