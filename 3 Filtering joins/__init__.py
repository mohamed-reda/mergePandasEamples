"""
Step 1 - semi join:(similar to an inner join, Returns only columns from the left table and not the right)
genres_tracks = genres.merge(top_tracks, on='gid')
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]

anti join: (indicator creates a new column that make says if that item at left_only or both or ...)
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]


try:
top_genres = genres[!genres['gid'].isin(genres_tracks['gid'])]



### Concatenate DataFrames together vertically
----------------------------------------------

Basic concatenation:
pd.concat([inv_jan, inv_feb, inv_mar])

Ignoring the index:
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True)

Setting labels to original tables (like group by with these keys: jan for the first table,....etc):
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, keys=['jan','feb','mar'])

Concatenate tables with different column names (concatenate but if there is a column not there in the other table,
    make the value of the item = NaN):
pd.concat([inv_jan, inv_feb], sort=True)

(add just the common columns):
pd.concat([inv_jan, inv_feb], join='inner')

Append the tables (.append() Simplified version of the .concat()
    Does Not Support: keys and join,
    Always join = outer (with NaN)):
inv_jan.append([inv_feb, inv_mar], ignore_index=True, sort=True)


Validating merges
# .merge(validate=None) : # Checks if merge is of specified type
# 'one_to_one'
# 'one_to_many'
# 'many_to_one'
# 'many_to_many':
tracks.merge(specs, on='tid', validate='one_to_one')


Verifying concatenations:
# Check whether the new concatenated index contains duplicates
# Default value is False:
pd.concat([inv_feb, inv_mar], verify_integrity=False)


---------------------------------------------------------------------------------------------------------
merge_ordered():
----------------

merge_ordered() method:
Column(s) to join on:
on , left_on , and right_on
Type of join:
how (left, right,inner, outer)
default :
outer
Overlapping column names:
suffixes
Calling the function:
pd.merge_ordered(df1, df2)

Merging stock data:
pd.merge_ordered(appl, mcd, on='date', suffixes=('_aapl','_mcd'))

Forward fill example (fill missing with previous value):
pd.merge_ordered(appl, mcd, on='date', suffixes=('_aapl','_mcd'), fill_method='ffill')

---------------------------------------------------------------------------------------------------------
merge_asof(): (Match on the nearest key column and not exact matches,
                Merged "on" columns must be sorted.
                Similar to a merge_ordered() left join)
-------------
#  Both DataFrames must be sorted by the key (if it's 5 and the right table has 4.5, 5.2, it will choose 4.5)
pd.merge_asof(visa, ibm, on='date_time',suffixes=('_visa','_ibm'))


here the nearest: (if it's 5 and the right table has 4.5, 5.2, it will choose 5.2)
pd.merge_asof(visa, ibm, on=['date_time'], suffixes=('_visa','_ibm'), direction='forward')

---------------------------------------------------------------------------------------------------------
Selecting data with.query()
----------------------------

stocks.query('nike > 90 and disney < 140')
stocks_long.query('stock=="disney" or (stock=="nike" and close < 90)')

---------------------------------------------------------------------------------------------------------
Reshaping data with.melt()
----------------------------
social_fin_tall = social_fin.melt(id_vars=['financial','company'])
print(social_fin_tall.head(10))

social_fin_tall = social_fin.melt(id_vars=['financial','company'], value_vars=['2018','2017'])

social_fin_tall = social_fin.melt(id_vars=['financial','company'],
value_vars=['2018','2017'],
var_name=['year'], value_name='dollars')



"""
# finished 5 from 36
print(96 - (96 * 16 / 100))
# still 80.64
# 68   +   ( 12 )
