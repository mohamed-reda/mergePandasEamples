"""
For clarity
Tables = DataFrames
Merging = Joining

>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
>> df.shape
(2, 2)

1 Inner join based on 'ward':
wards_census = wards.merge(census, on='ward')
print(wards_census.head(4))

Suffixes: ( if we have 2 columns has the sae name, add to the column of wards 'wards', .. etc)
wards_census = wards.merge(census, on='ward', suffixes=('_ward','_cen'))
print(wards_census.head())
print(wards_census.shape)

# Group the results by title then count the number of accounts:
about agg:
for the column that could account, use the method cound
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

Single merge:
grants.merge(licenses, on=['address','zip'])



Merging multiple tables
grants_licenses_ward = grants.merge(licenses, on = ['address','zip']).merge(wards, on='ward',
 suffixes=('_bus','_ward'))


















"""
