import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split
import pickle
import json


# Load data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Collaborative Filtering Model
def train_collaborative_filtering():
    reader = Reader(rating_scale=(0.5, 5))
    data = Dataset.load_from_df(ratings[['UserID', 'MovieID', 'Rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    predictions = model.test(testset)
    rmse=accuracy.rmse(predictions)

    with open("models/cf_model.pkl", "wb") as f:
        pickle.dump(model, f)

# Content-Based Filtering Model
def train_content_based_filtering():
    tfidf = TfidfVectorizer(stop_words="english")
    movies['Genres'] = movies['Genres'].fillna('')
    tfidf_matrix = tfidf.fit_transform(movies['Genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    with open("models/content_model.pkl", "wb") as f:
        pickle.dump((cosine_sim, movies), f)

# Hybrid Filtering Model
def train_hybrid_filtering():
    train_collaborative_filtering()
    train_content_based_filtering()
    hybrid_metrics={}

if __name__ == "__main__":
    train_collaborative_filtering()
    train_content_based_filtering()
    train_hybrid_filtering()
