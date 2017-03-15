"""
 hw1.py Created by baobao on 3/15/17.
"""
import pandas as pd
import numpy
import time
from lshash import LSHash
from sklearn.neighbors import NearestNeighbors

data = pd.read_csv("Traj_1000_SH_UTM")
print data

x = 840
y = 760
length = 44017
matrix = [[0 for i in range(1000)] for i in range(44107)]
tempArray = [0 for i in range(x * y)]

'''
timelist = list(data["Time"])
for d in timelist:
    timeArray = time.strptime(d, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(timeArray))
    data.iloc[i, 1] = timestamp
    '''
for index, row in data.iterrows():
    tempArray[int((row[3] - 3448600) / 20) * int((row[2] - 346000) / 20)] = 1
print data

i = 1
for a in tempArray:
    if a == 1:
        a = i
        i += 1

Tid = 1
while Tid <= 1000:
    trace = data.loc[(data['Tid'] == Tid), ['Time', 'X', 'Y']]
    for index,row in trace.iterrows():
        matrix[Tid][tempArray[int(row[1] * row[2])]] = 1
    Tid += 1
print matrix

lsh = LSHash(4, length)
for row in matrix:
    lsh.index(row)
result = lsh.query(matrix[0])
for row in result:
    print row[1]

'''
nbrs = NearestNeighbors(n_neighbors=3).fit(data)
nbrs.kneighbors()
'''