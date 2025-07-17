# Netflix Movie Recommender System

This project is a simple content-based movie recommender system inspired by the Netflix dataset from Kaggle. It takes in a movie title and suggests similar movies based on their plot descriptions, using natural language processing techniques. The goal of this project is to demonstrate my skills in building machine learning-based applications from scratch and deploying them with an interactive web interface.

---

## Live Demo

You can try the app here:
https://916dc1059b11374bee.gradio.live

---

## Project Summary

This recommender system works by analysing the movie descriptions and identifying similarities between different titles. It was built using:

- Python for the backend logic
- Pandas and scikit-learn for data processing and modelling
- Gradio for the user interface

Given a movie title, the app returns a list of recommended titles along with their genres and descriptions.

---

## How It Works

1. **Dataset**: A public dataset of Netflix titles was used, which includes columns like `title`, `description`, and `listed_in` (genre).
2. **Preprocessing**:
   - Missing values are removed.
   - The title, genre, and description are combined into a single text field.
   - Dupliacte values are removed.
   - All text is converted to lowercase to ensure uniformity.
3. **TF-IDF Vectorization**:
   - Converts movie content into numerical vectors while removing common stopwords.
   - Both single words and two-word phrases are considered using `ngram_range=(1, 2)`.
4. **Cosine Similarity**:
   - Calculates similarity scores between all movies.
   - For any given movie title, the top 5 most similar titles are retrieved.
5. **Interface**:
   - A minimal and clean user interface is built using Gradio.
   - Users simply input a movie title to get suggestions.

---

## Features

- Case-insensitive search
- Lightweight and fast
- Uses content-based filtering (no user data or ratings needed)
- Runs entirely in the browser via a public link

---

## Possible Future Enhancements

- Add filters for genre or release year
- Switch to collaborative filtering based on ratings
- Include movie trailer links
- Host on a permanent server for wider accessibility

---

This project is for educational and demonstration purposes.

