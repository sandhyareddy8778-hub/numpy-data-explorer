import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- STEP 1: LOAD FULL PRODUCTION DATASET ---
FILE_PATH = 'netflix_titles.csv'

# If you don't have the file locally, this downloads the official 8,800+ row dataset
if not os.path.exists(FILE_PATH):
    print("Local 'netflix_titles.csv' not found. Fetching official dataset...")
    url = "https://huggingface.co/datasets/hugginglearners/netflix-shows/resolve/main/netflix_titles.csv"
    df = pd.read_csv(url)
    df.to_csv(FILE_PATH, index=False)
else:
    df = pd.read_csv(FILE_PATH)

# Clean dataset column strings to avoid spacing bugs
df['type'] = df['type'].str.strip()
df['listed_in'] = df['listed_in'].fillna('Unknown')

# --- STEP 2: RE-ENGINEER GENRES & DATA OVERVIEW ---
# Extract primary genre safely
df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0].strip())
top_genres = df['main_genre'].value_counts().head(10)

print(f"Successfully loaded production dataset with {df.shape[0]} titles!")

# --- STEP 3: CONSTRUCT THE 2X2 METRIC DASHBOARD ---
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

# Plot 1: Content Growth Over Time (Post-2000)
# Showing thousands of files over a cleaner timescale
recent_df = df[(df['release_year'] > 2000) & (df['release_year'] < 2022)]
sns.countplot(data=recent_df, x='release_year', hue='type', ax=axes[0, 0], palette='magma')
axes[0, 0].set_title('Content Growth Over Time (Post-2000)', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Release Year')
axes[0, 0].set_ylabel('Number of Titles')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Top 10 Content Genres
# Filling the bars completely with large-scale value counts
sns.barplot(x=top_genres.values, y=top_genres.index, ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Top 10 Content Genres', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Number of Titles')
axes[0, 1].set_ylabel('Main Genre')

# Plot 3: Movie Runtime Distribution
# Parsing out the real numeric lengths (e.g. from '90 min') to show the real bell curve
movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_min'] = movies_df['duration'].str.extract('(\d+)').astype(float)
movies_df = movies_df[movies_df['duration_min'].between(30, 200)].dropna(subset=['duration_min'])

sns.histplot(data=movies_df, x='duration_min', bins=30, kde=True, ax=axes[1, 0], color='crimson')
axes[1, 0].set_title('Movie Runtime Distribution', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Runtime (Minutes)')
axes[1, 0].set_ylabel('Number of Movies')

# Plot 4: Top TV Show Season Counts
# Accurately shows '1 Season' as the top trend on the platform
tv_df = df[df['type'] == 'TV Show'].copy()
top_seasons = tv_df['duration'].str.strip().value_counts().head(5)

sns.barplot(x=top_seasons.values, y=top_seasons.index, ax=axes[1, 1], palette='rocket')
axes[1, 1].set_title('Top TV Show Season Counts', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Number of TV Shows')
axes[1, 1].set_ylabel('Duration')

# Adjust presentation and export
plt.tight_layout()
plt.savefig('correct_netflix_eda_report.png', dpi=300)
plt.show()