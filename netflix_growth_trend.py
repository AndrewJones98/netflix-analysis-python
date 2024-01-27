import pandas as pd
import plotly.express as px

df = pd.read_csv('netflix_titles.csv')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

unparsed_entries = df[df['date_added'].isna()]

content_added_per_year = df.groupby('year_added').size().reset_index(name='count')

fig = px.line(content_added_per_year, x='year_added', y='count', 
              title='Content Added Over Time',
              labels={'year_added': 'Year Added', 'count': 'Number of Contents Added'})

fig.show()
