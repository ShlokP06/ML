import pandas as pd
import numpy as np
import pickle
import warnings

def hybrid_recommendation(user_id, title, svd, tfidf, user_movie_matrix, content_similarity, movies, top_n=5):
    if user_id not in user_movie_matrix.index:
        return ["User not found"], None

    user_ratings = user_movie_matrix.loc[user_id].values.reshape(1, -1)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        user_ratings_reduced = svd.transform(user_ratings)

    if user_ratings_reduced is None or user_ratings_reduced.size == 0:
        return ["SVD transformation failed"], None

    predicted_ratings = np.dot(user_ratings_reduced, svd.components_)
    predicted_ratings = pd.Series(predicted_ratings[0], index=user_movie_matrix.columns)
    
    if predicted_ratings.isnull().all():
        return ["No predictions available"], predicted_ratings
    if title not in movies['Title'].values:
        return ["Title not found"], predicted_ratings

    movie_index = movies[movies['Title'] == title].index[0]
    if movie_index >= len(content_similarity):
        return ["Invalid movie index"], predicted_ratings
    similar_movies = list(enumerate(content_similarity[movie_index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:top_n+1]
    similar_movies = [movies.iloc[i[0]]['Title'] for i in similar_movies]
    valid_similar_movies = [movie for movie in similar_movies if movie in predicted_ratings.index]

    if not valid_similar_movies:
        return ["No valid recommendations"], predicted_ratings
    hybrid_recommendations = predicted_ratings[valid_similar_movies].sort_values(ascending=False)
    return hybrid_recommendations.index.tolist(), predicted_ratings
