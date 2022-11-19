"""
Merge with left join:
movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

Merge with right join:
tv_movies = movies.merge(tv_genre, how='right', left_on='id', right_on='movie_id')

Merge with outer join:
family_comedy = family.merge(comedy, on='movie_id', how='outer', suffixes=('_fam', '_com'))

Merging a table to itself:
original_sequels = sequels.merge(sequels, left_on='sequel', right_on='id', suffixes=('_org','_seq'))

Merging a table to itself with left join:
original_sequels = sequels.merge(sequels, left_on='sequel', right_on='id', how='left', suffixes=('_org','_seq'))

Setting an index:
movies = pd.read_csv('tmdb_movies.csv', index_col=['id'])

Merging on index:
movies_taglines = movies.merge(taglines, on='id', how='left')

MultiIndex datasets
samuel = pd.read_csv('samuel.csv', index_col=['movie_id', 'cast_id'])

MultiIndex merge:
samuel_casts = samuel.merge(casts, on=['movie_id','cast_id'])

Index merge with left_on and right_on: -----------------------------
movies_genres = movies.merge(movie_to_genres, left_on='id', left_index=True, right_on='movie_id', right_index=True)





##### Create an index that returns true if name_1 or name_2 are null, so this | means or:
m = ((iron_1_and_2['name_1'].isnull()) | (iron_1_and_2['name_2'].isnull()))








movie_to_genres = pd.read_csv('tmdb_movie_to_genres.csv')
tv_genre = movie_to_genres[movie_to_genres['genre'] == 'TV Movie']
print(tv_genre)

Continue format results:
print(original_sequels[,['title_org','title_seq']].head())
"""
