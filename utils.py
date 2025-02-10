import pickle
import numpy as np
import pandas as pd
from surprise import accuracy
from sklearn.metrics import mean_squared_error,precision_score, recall_score, f1_score

# Load Collaborative Filtering Model
def load_cf_model():
    with open("models/cf_model.pkl", "rb") as f:
        return pickle.load(f)

# Load Content-Based Filtering Model
def load_content_model():
    with open("models/content_model.pkl", "rb") as f:
        return pickle.load(f)

# Collaborative Filtering Recommendations
def cf_recommendations(user_id, model, movies, ratings, n=5):
    user_ratings = ratings[ratings['UserID'] == user_id]
    user_unrated_movies = movies[~movies['MovieID'].isin(user_ratings['MovieID'])].copy()
    user_unrated_movies = user_unrated_movies.copy()
    user_unrated_movies.loc[:,'predicted_rating'] = user_unrated_movies['MovieID'].apply(lambda x: model.predict(user_id, x).est)
    return user_unrated_movies.sort_values(by='predicted_rating', ascending=False).head(n)

# Content-Based Filtering Recommendations
def content_recommendations(title, cosine_sim, movies, n=5):
    idx = movies[movies['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices]

# Hybrid Recommendations
def hybrid_recommendations(user_id, title, cf_model, cosine_sim, movies, ratings, n=5):
    cf_recs = cf_recommendations(user_id, cf_model, movies, ratings, n)
    content_recs = content_recommendations(title, cosine_sim, movies, n)
    hybrid_recs = pd.concat([cf_recs, content_recs]).drop_duplicates().head(n)
    return hybrid_recs
