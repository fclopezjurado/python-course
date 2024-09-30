import pandas

from lesson6.pandas_module_usage import dataframe1

dataframe = pandas.DataFrame({
    2016: [4.322, 5.717, 7.796, 30.339],
    2017: [5.07, 6.618, 7.502, 27.732],
    2018: [3.857, 4.5, 7.14, 21.985]
}, index=['Santander', 'BBVA', 'Telefónica', 'Inditex'])

print(dataframe)
print()
print(dataframe.info())
print()
print(dataframe.columns)
print()
print(dataframe.columns.values)
print()
print(dataframe.first_valid_index)
print()
print(dataframe.index.values)
print()
print(dataframe.describe())
print()
print(dataframe.shape)
print()
print(len(dataframe))
print()
print(len(dataframe.columns))
