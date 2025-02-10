from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
from utils import hybrid_recommendation 
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)
# Load models and data
with open('svd_model.pkl', 'rb') as f:
    svd = pickle.load(f)

with open('tfidf_model.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('user_movie_matrix.pkl', 'rb') as f:
    user_movie_matrix = pickle.load(f)

with open('content_similarity.pkl', 'rb') as f:
    content_similarity = pickle.load(f)

with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = int(data['user_id'])
    title = data['title']
  
    if not user_id or not title:
        return jsonify({"error": "Missing user_id or title"}), 400
    recommendations,predicted_ratings = hybrid_recommendation(user_id, title, svd, tfidf, user_movie_matrix, content_similarity, movies)
    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)
