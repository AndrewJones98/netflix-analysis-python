import pandas as pd
import plotly.express as px

df = pd.read_csv('netflix_titles.csv')

df['country'] = df['country'].fillna('Unknown')
df['listed_in'] = df['listed_in'].fillna('Unknown')

df_countries = df.assign(country=df['country'].str.split(',')).explode('country')
df_countries['country'] = df_countries['country'].str.strip()

df_countries_genres = df_countries.assign(genre=df_countries['listed_in'].str.split(',')).explode('genre')
df_countries_genres['genre'] = df_countries_genres['genre'].str.strip()

country_genre_count = df_countries_genres.groupby(['country', 'genre']).size().reset_index(name='count')

fig = px.density_heatmap(country_genre_count, x='genre', y='country', z='count', 
                         title='Genre Specialization by Country', 
                         labels={'count': 'Number of Titles'},
                         color_continuous_scale='Viridis')

fig.show()
