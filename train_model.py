import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import pickle
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
data = pd.merge(ratings, movies, on='MovieID')

user_movie_matrix = data.pivot_table(index='UserID', columns='Title', values='Rating').fillna(0)
svd = TruncatedSVD(n_components=50, random_state=42)
user_movie_matrix_reduced = svd.fit_transform(user_movie_matrix)

tfidf = TfidfVectorizer(stop_words='english')
movies['Genres'] = movies['Genres'].str.replace('|', ' ')
genre_matrix = tfidf.fit_transform(movies['Genres'])

content_similarity = cosine_similarity(genre_matrix, genre_matrix)
with open('svd_model.pkl', 'wb') as f:
    pickle.dump(svd, f)

with open('tfidf_model.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

with open('user_movie_matrix.pkl', 'wb') as f:
    pickle.dump(user_movie_matrix, f)

with open('content_similarity.pkl', 'wb') as f:
    pickle.dump(content_similarity, f)

with open('movies.pkl', 'wb') as f:
    pickle.dump(movies, f)

print("Models and data saved successfully!")
