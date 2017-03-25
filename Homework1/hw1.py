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
length = 1000
target = 69
'''
    target is the trace for lsh and knn
'''

matrix = [[0 for i in range(44107)] for i in range(1000)]
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

i = 1
for a in tempArray:
    if a == 1:
        a = i
        i += 1

Tid = 0
while Tid < 1000:
    trace = data.loc[(data['Tid'] == Tid + 1), ['Time', 'X', 'Y']]
    for index, row in trace.iterrows():
        matrix[Tid][tempArray[int((row[2] - 3448600) / 20) * int((row[1] - 346000) / 20)]] = 1
    Tid += 1

lsh = LSHash(20000, 44107)
for element in matrix:
    lsh.index(element)
result = lsh.query(matrix[target - 1])
for row in result:
    print row

nbrs = NearestNeighbors(n_neighbors=20)
nbrs.fit(matrix)
print nbrs.kneighbors(matrix[target - 1])
