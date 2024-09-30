from numpy.random import normal, randint
import pandas

ROWS = 5
COLUMNS = 20
AVERAGE = 5
STANDARD_DEVIATION = 2

indexes = ['row' + str(row) for row in range(0, ROWS)]
columns = ['column' + str(column) for column in range(0, COLUMNS)]

def generateSeriesUsingNormalDistribution():
    return [
        [normal(AVERAGE, STANDARD_DEVIATION, size=1)[0] for column in range(0, COLUMNS)]
        for row in range(0, ROWS)
    ]

def generateSeriesUsingUniformDistribution():
    return [randint(0, 9, COLUMNS) for row in range(0, ROWS)]

dataframe1 = pandas.DataFrame(generateSeriesUsingNormalDistribution(), index=indexes, columns=columns)
dataframe2 = pandas.DataFrame(generateSeriesUsingUniformDistribution(), index=indexes, columns=columns)

print(dataframe1)
print(dataframe2)
