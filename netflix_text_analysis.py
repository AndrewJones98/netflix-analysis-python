import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv('netflix_titles.csv')

def preprocess_text(text):

    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word.isalpha()]
    return tokens

df['processed_description'] = df['description'].apply(preprocess_text)

all_words = [word for tokens in df['processed_description'] for word in tokens]
all_words_freq = Counter(all_words)
most_common_words = all_words_freq.most_common(10)

print("Most Common Words Across All Movies:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")


top_genres = df['listed_in'].str.split(',').explode().str.strip().value_counts().head(10).index

def get_genre_keywords(df, genre):
    genre_df = df[df['listed_in'].str.contains(genre, case=False, na=False)]
    all_words = [word for tokens in genre_df['processed_description'] for word in tokens]
    frequency_dist = Counter(all_words)
    return frequency_dist.most_common(10)

top_words_per_genre = {}

for genre in top_genres:
    top_words_per_genre[genre] = get_genre_keywords(df, genre)

for genre, top_words in top_words_per_genre.items():
    print(f"\nTop words in {genre} genre:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

with open('output.txt', 'w') as file:

    file.write("Most Common Words Across All Movies:\n")
    for word, freq in most_common_words:
        file.write(f"{word}: {freq}\n")

    file.write("\n")

    for genre in top_genres:
        top_words_per_genre = get_genre_keywords(df, genre)
        file.write(f"\nTop words in {genre} genre:\n")
        for word, freq in top_words_per_genre:
            file.write(f"{word}: {freq}\n")

