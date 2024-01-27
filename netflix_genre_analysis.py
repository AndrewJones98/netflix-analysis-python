import pandas as pd
import plotly.express as px


df = pd.read_csv('netflix_titles.csv')


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year


df_genres = df.assign(genre=df['listed_in'].str.split(',')).explode('genre')
df_genres['genre'] = df_genres['genre'].str.strip()


top_genres = df_genres['genre'].value_counts().head(10).index


df_top_genres = df_genres[df_genres['genre'].isin(top_genres)]


genre_trends = df_top_genres.groupby(['year_added', 'genre']).size().reset_index(name='count')


fig = px.line(genre_trends, x='year_added', y='count', color='genre', 
              title='Trend of Top 10 Genres by Date Added',
              labels={'year_added': 'Year Added', 'count': 'Number of Shows/Movies'})


fig.show()
