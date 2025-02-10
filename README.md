# GDSC-ML
GDSC IIT Indore induction task under ML
# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** built using **Collaborative Filtering, Content-Based Filtering, and Hybrid Filtering** techniques. It takes user input and recommends movies based on preferences and historical interactions.

## Features
- **Collaborative Filtering (CF):** Uses **Matrix Factorization (SVD)** to suggest movies based on user ratings.
- **Content-Based Filtering:** Uses **TF-IDF and Cosine Similarity** to recommend movies similar to a given title.
- **Hybrid Filtering:** Combines both methods for better accuracy.
- **Flask API:** Exposes endpoints to fetch movie recommendations.
- **Pretrained Models:** Trained models for quick inference.

## Tech Stack
- **Python** (Flask, Pandas, NumPy, scikit-learn, Surprise, Pickle)
- **Machine Learning** (Collaborative Filtering, Content-Based Filtering)
- **Frontend** (HTML, CSS, JavaScript)

## Dataset
The repository contains a script `dn_movies.py` that needs to be run to download `ratings.csv`. Additionally, `movies.csv` is included in the repository.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download the dataset:
   ```sh
   python dn_movies.py
   ```
4. Train the models (optional):
   ```sh
   python train_model.py
   ```

## Running the Application
To start the Flask app, follow these steps:
1. Ensure all dependencies are installed.
2. Train the models if not already trained:
   ```sh
   python train_model.py
   ```
3. Start the Flask application:
   ```sh
   python app.py
   ```
4. Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
5. Use the interface or send a POST request to `/recommend` for movie recommendations.

## API Endpoints
- **GET `/`**: Renders the homepage.
- **POST `/recommend`**: Accepts JSON input and returns movie recommendations.

## Directory Structure
```
├── app.py                  # Flask application
├── train_model.py          # Model training script
├── utils.py                # Utility functions
├── models/                 # Stored models
├── templates/
│   ├── index.html          # Frontend UI
├── static/
│   ├── css/
│   │   ├── styles.css      # Stylesheet
│   ├── js/
│   │   ├── script.js       # JavaScript file
├── dn_movies.py            # Script to download ratings.csv
├── movies.csv              # Movies dataset
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```

## Future Improvements
- Add **Deep Learning-based Recommendations**.
- Enhance **UI/UX** for a better user experience.
- Deploy the app on **Heroku/AWS**.

## Download
- [Download README.md](README.md)
- [Download requirements.txt](requirements.txt)

