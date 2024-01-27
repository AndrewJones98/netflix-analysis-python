import pandas as pd
import plotly.express as px

df = pd.read_csv('netflix_titles.csv')

df_movies = df[df['type'] == 'Movie']

df_movies['duration'] = df_movies['duration'].str.replace(' min', '').astype(float)

df_movies = df_movies.dropna(subset=['duration'])

df_movies['duration'] = df_movies['duration'].astype(int)

df_movies_genres = df_movies.assign(genre=df_movies['listed_in'].str.split(',')).explode('genre')
df_movies_genres['genre'] = df_movies_genres['genre'].str.strip()

fig = px.box(df_movies_genres, x='genre', y='duration', 
             title='Comparison of Movie Durations Across Genres',
             labels={'duration': 'Duration (minutes)', 'genre': 'Genre'})

fig.show()