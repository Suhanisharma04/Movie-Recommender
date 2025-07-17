import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr

df =pd.read_csv("netflix_titles.csv")
print(df.columns)
df = df[["title", "description", "listed_in"]].dropna()
df['content'] = df['description'] + " " + df['listed_in']
df['content'] = df['content'].str.lower()
print(df.head())

#converting descriptions to vectors
tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2)) #ignoring words like "is" that are common
tfidf_matrix = tfidf.fit_transform(df['content']) #converting text to numeric form

# measuring similarity between movie descriptions
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# creating index for movie title
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()


def recommend_movie(title):
    title = title.lower()
    if title not in indices:
        return "Movie not found. Try another title!"

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]

    recommendations = []
    for i in movie_indices:
        movie_title = df.iloc[i]['title']
        genre = df.iloc[i]['listed_in']
        desc = df.iloc[i]['description']
        rec = f"🎬: {movie_title}\n 📚: {genre}\n 📝: {desc}\n"
        recommendations.append(rec)

    return "\n\n".join(recommendations)

#gradio interface
iface = gr.Interface(
    fn=recommend_movie,
    inputs=gr.Textbox(lines=1, placeholder="Enter a movie title..."),
    outputs="text",
    title="Netflix Movie Recommender",
    description="Type a movie name to get 5 similar recommendations with genre and description.",
    theme="soft",
)
iface.launch(share=True)