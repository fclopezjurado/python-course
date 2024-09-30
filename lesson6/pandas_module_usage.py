import pandas
import numpy
from pandas.core.window.doc import numba_notes
from sqlalchemy.util import OrderedDict
from sympy import series

series1 = pandas.Series(numpy.array(['a', 'b', 'c', 'd', 'e'])) # numpy array
series2 = pandas.Series([1, 2, 3, 4, 5]) # list with integers
series3 = pandas.Series([1.1, 2.2, 3.3, 4.4, 5.5]) # list with floats
series4 = pandas.Series([1, 2, 3, 4, 5], dtype=float) # list with integers and float dtype
series5 = pandas.Series([1, 2, 3, 4, 5], dtype=numpy.int8) # list with integers and int8 dtype
series6 = pandas.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']) # list with integers and custom indexes

new_indexes_for_series1 = ['odd1', 'even1', 'odd2', 'even2', 'odd3']
series1.index = new_indexes_for_series1 # update indexes for series1

dictionary1 = {'d': 4, 'c': 3, 'b': 2, 'a': 1}
series7 = pandas.Series(dictionary1) # create series from dictionary1
series8 = series7.copy() # copy series7 to series8

print(series1)
print(series2)
print(series3)
print(series4)
print(series5)
print(series6)
print(series7)
print(series8)

pandas.Series(0, index = range(5)) # create series with 5 zeros
pandas.Series(0, range(5)) # create series with 5 zeros

if 'c' in series7:
    print('c is in series7')

print(series1['odd1']) # get element by index
print(series2[2]) # get element by index
print(series3[2]) # get element by index
print(len(series1)) # get length of series1
print(series1.describe) # get statistics of series1
print(series1.value_counts()) # get count of unique values in series1
print(series1.index) # get indexes of series1
print(series1.values) # get values of series1

series9 = pandas.Series([1, 5, 2, 7, 3, 2, 5, 8, 1, 4, 7, 2, 5, 3, 6, 1, 2, 7])
series9_description = series9.describe()
series9_value_counts = series9.value_counts()
series9_indexes = series9.index
series9_values = series9.values

print(series9_description)
print(series9_value_counts)
print(series9_indexes)
print(series9_values)

dictionary2 = {'1': [1], '2': [2, 3], '3': [3, 4, 5], '4': [4, 5, 6, 7]}
series10 = pandas.Series(dictionary2)
series10_description = series10.describe()
series10_value_counts = series10.value_counts()
series10_indexes = series10.index
series10_values = series10.values

print(series10)
print(series10_description)
print(series10_value_counts)
print(series10_indexes)
print(series10_values)

series11 = series2 + series3 # add series2 and series3 number by number
series12 = series2 * 2 # multiply series2 by 2
series13 = series2 ** 2 # square series2
series14 = numpy.log(series2) # get natural logarithm of series2
series15 = numpy.cos(series2) # get cosine of series2

print(series11)
print(series12)
print(series13)
print(series14)
print(series15)

series16 = pandas.Series([2, 4, 6, 1])
series17 = pandas.Series([1, 2, 3, 4])

print(series16 == series17) # compare series16 and series17 element by element
print(series16 > series17) # compare series16 and series17 element by element
print(series16 < series17) # compare series16 and series17 element by element

list_series16 = series16.tolist() # convert series17 to list
dictionary_series16 = series16.to_dict() # convert series16 to dictionary
ordered_dictionary_series16 = series16.to_dict(OrderedDict) # convert series16 to ordered dictionary
list1 = [['one', 'two', 'three'], ['four', 'five'], ['six'], ['seven']]
series_from_list = pandas.Series(list1) # create series from list

print(series_from_list)

series_from_list = series_from_list.apply(pandas.Series).stack().reset_index(drop=True) # new series resetting indexes

print(list_series16)
print(dictionary_series16)
print(series_from_list)
print(ordered_dictionary_series16)

series18 = pandas.Series([1, 2, 3, 4, 5, 6, numpy.inf, numpy.nan])
series19 = pandas.Series([1, 2, 3, 4, 5, 6, numpy.inf, numpy.nan])
series20 = pandas.Series([1, 2, 3, 4, 5, 6, numpy.inf, numpy.nan])
series18[series18 < 3] = 0 # set elements less than 3 to 0
series19[series19 == numpy.inf] = 0 # set elements equal to infinity to 0
series20[numpy.isnan(series20)] = 10 # set elements equal to NaN to 10
subseries1 = series18[series18 > 3] # get subseries with elements greater than 3

print(series18)
print(series19)
print(series20)
print(numpy.nan == numpy.nan) # compare NaN with NaN
print(numpy.all(series4 == series5)) # check if all series elements are equals
print(numpy.any(series4 == series5)) # check if any series elements are equals
print(series16.sort_values()) # sort series16 values
print(series16.idxmax()) # get index of maximum element in series16

print(series18[2:4]) # prints a new subseries from series7 elements from index 2 to 4
print(series18[:3]) # prints a new subseries from series7 elements from index 0 to 3
print(series18[3:]) # prints a new subseries from series7 elements from index 3 to the end
print(series18[[0, 2, 3]]) # prints a new subseries from series7 elements with indexes 0, 2 and 3
print(series18.iloc[2]) # prints element with index 2
print(series18.iloc[2:4]) # prints a new subseries from series7 elements from index 2 to 4
print(subseries1) # prints subseries1. Indexes from series18 were preserved

series21 = pandas.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
series22 = pandas.Series([5, 6, 7, 8], ['a', 'd', 'e', 'f'])
series23 = pandas.Series([6, 1, 2, 7, 0, numpy.inf, 1, numpy.nan, numpy.nan])

print(series21 + series22) # add series21 and series22 number by number
print(series23.dropna()) # drop NaN values from series23
print(series23.fillna(1)) # replace NaN values by once's in series23

series23_indexes = ['number1', 'number2', 'number3', 'number4', 'number5', 'number6', 'number7', 'number8', 'number9']
series23.index = series23_indexes # update indexes for series23

print(series23.filter(items=['number1', 'number2', 'number3'])) # filter series23 by indexes
print(series23.filter(like='number')) # filter series23 by numbers (indexes)
print(series23.filter(regex='[0-5]')) # filter series23 by [0-9] regex in indexes

def square(value):
    return value ** 2

print(series23.apply(square)) # apply square function to series23
print(series23.apply(lambda value: value * 4)) # apply lambda function to series23

dataframe1_series = numpy.array([[1.5, 3, 3.4, 9], [3.4, 5, 3.6, 1.2], [5.2, 1, 2.8, 3.9]])
dataframe1 = pandas.DataFrame(dataframe1_series, index=['a1', 'a2', 'a3'], columns=['A', 'B', 'C', 'D'])
dataframe2 = pandas.DataFrame({'A': [1.5, 3.4, 5.2], 'B': [3, 5, 1], 'C': [3.4, 3.6, 2.8], 'D': [9, 1.2, 3.9]},
                              index=['a1', 'a2', 'a3'])
dataframe3 = pandas.DataFrame({'A': [1.5, 3.4, 5.2], 'B': [3, 5, 1], 'C': [3.4, 3.6, 2.8], 'D': [9, 1.2, 3.9]},
                              columns = ['A', 'B', 'C', 'D'])
dataframe4 = pandas.DataFrame([{'A': 1.5, 'B': 3, 'C': 3.4, 'D': 9}, {'A': 3.4, 'B': 5, 'C': 3.6, 'D': 1.2},
                               {'A': 5.2, 'B': 1, 'C': 2.8, 'D': 3.9}])

dataframe4.reindex(columns=['C', 'B', 'A'], index=['a2', 'a3'])

print(dataframe1.info()) # get information about dataframe1
print(dataframe1.head(2)) # get first 2 rows of dataframe1
print(dataframe1.head()) # get first 5 rows of dataframe1
print(dataframe1.tail(2)) # get last 2 rows of dataframe1
print(dataframe1.columns) # get columns names of dataframe1
print(dataframe1.columns.values) # get columns values of dataframe1
print(dataframe1.index) # get indexes of dataframe1
print(dataframe1.index.values) # get indexes values of dataframe1
print(dataframe1.describe()) # get statistics of dataframe1
print(dataframe1.shape) # get shape of dataframe1
print(len(dataframe1)) # get length of dataframe1
print(len(dataframe1.columns)) # get length of dataframe1 columns
