import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("movies.csv")

# Convert genres into feature vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["genres"].fillna(""))

# Compute similarity scores
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Movie recommendation function
def recommend_movie(movie_title):
    if movie_title not in movies["title"].values:
        return ["Movie not found! Please try another."]
    
    # Get the index of the selected movie
    idx = movies[movies["title"] == movie_title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]  # Top 3 similar movies
    
    # Get movie recommendations
    movie_indices = [i[0] for i in sim_scores]
    return movies["title"].iloc[movie_indices].tolist()

# Example usage
movie_name = input("Enter a movie name: ")
recommendations = recommend_movie(movie_name)
print("Recommended Movies:", recommendations)
