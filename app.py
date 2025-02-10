from flask import Flask, render_template, request, jsonify
import utils
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    user_id = int(data.get("userId"))
    title = data.get("title")
    method = data.get("method")

    if method == "CF":
        model = utils.load_cf_model()
        movies = pd.read_csv("movies.csv")
        ratings = pd.read_csv("ratings.csv")
        recs = utils.cf_recommendations(user_id, model, movies, ratings)
    elif method == "Content":
        cosine_sim, movies = utils.load_content_model()
        recs = utils.content_recommendations(title, cosine_sim, movies)
    elif method == "Hybrid":
        cf_model = utils.load_cf_model()
        cosine_sim, movies = utils.load_content_model()
        ratings = pd.read_csv("ratings.csv")
        recs = utils.hybrid_recommendations(user_id, title, cf_model, cosine_sim, movies, ratings)

    return jsonify(recs.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)