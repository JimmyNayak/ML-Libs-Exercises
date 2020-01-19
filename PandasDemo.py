import pandas as pd

# series = pd.Series([1, 2, 4, 5, 6, 8])
#
# print(series)
#
# print(series.head())


info = pd.read_csv("http://bit.ly/uforeports")
# print(info)
# print(info.head(10))

# print(info['State'])

# info['Location'] = info.City + ',' + info.State
#
# print(info.head())

# print(info.shape)

# print(info.describe())

# print(info.dtypes)

# print(info.columns)

# info.drop('Colors Reported',axis=1,inplace=True)
#
# print(info.head())

# print(info['State'].sort_values(ascending=False).head())

# print(info['State'].sort_values(ascending=True).head())

print(info.sort_values(ascending=True, by='City').head(50))
