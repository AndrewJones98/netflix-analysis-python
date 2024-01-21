import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

unparsed_entries = df[df['date_added'].isna()]
print("Unparsed Entries:\n", unparsed_entries)

content_added_per_year = df.groupby('year_added').size()

sns.set(style="whitegrid")

plt.figure(figsize=(12,6))
sns.lineplot(data=content_added_per_year)
plt.title('Content Added Over Time')
plt.xlabel('Year Added')
plt.ylabel('Number of Contents Added')
plt.show()
