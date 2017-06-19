# coding=utf-8
"""
    Created by AMXPC on 2017/6/18.
"""
import numpy as np
import ReadData
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import NearestNeighbors


# 定义随机森林回归使用的数据对象
# 包含基站ID、经纬度，以及所有以该基站为主基站的MR记录的相对位置和信号强度(train)
# 包含基站ID、经纬度，以及所有以该基站为主基站的MR记录的实际位置和信号强度(test)


class RandomF:
    def __init__(self, station):
        self.station = station
        self.mr = []
        self.model = 0

    def addmr(self, mr, istest):
        if istest:
            self.mr.append(mr)
        else:
            longitude = mr[0] - self.station[2]
            latitude = mr[1] - self.station[3]
            self.mr.append([longitude, latitude, mr[2]])

    def addrf(self, model):
        self.model = model

    def issame(self, mr):
        if self.station[0] == mr[0] and self.station[1] == mr[1]:
            return True
        return False

    def display(self):
        print self.station, self.mr

# 获取数据
print "reading data..."
train_data = ReadData.readpt("data/final_2g_tr.csv")
# train_data = np.loadtxt(open("2gpt.csv", "rb"), delimiter=",", skiprows=0)
test_data = ReadData.readpt("data/final_2g_te.csv")
# test_data = np.loadtxt(open("2gte.csv", "rb"), delimiter=",", skiprows=0)
station_data = ReadData.readgc_2g("data/final_2g_gongcan.csv")
# station_data = np.loadtxt(open("2ggc.csv", "rb"), delimiter=",", skiprows=0)

# 根据主基站对训练集分组
print "spliting data..."
grouped_train = []
for i in range(train_data.shape[0]):
    added = False
    for j in range(len(grouped_train)):
        if grouped_train[j].issame(train_data[i, 0:2]):
            grouped_train[j].addmr(train_data[i, 2:5], istest=False)
            added = True
            break
    if not added:
        for k in range(station_data.shape[0]):
            if station_data[k][0] == train_data[i][0] and station_data[k][1] == train_data[i][1]:
                rf = RandomF(station_data[k])
                grouped_train.append(rf)
                grouped_train[-1].addmr(train_data[i, 2:5], istest=False)
                break
# print len(grouped_train), grouped_train[0].display()

# 对测试集分组
grouped_test = []
for i in range(len(grouped_train)):
    rf = RandomF(grouped_train[i].station)
    grouped_test.append(rf)
    for j in range(test_data.shape[0]):
        if grouped_test[-1].issame(test_data[j, 0:2]):
            grouped_test[-1].addmr(test_data[j, 2:5], istest=True)
# print len(grouped_test), grouped_test[0].display()

# 筛选测试集数据非空的随机森林组
i = 0
while True:
    if i >= len(grouped_train):
        break
    if len(grouped_test[i].mr) == 0:
        grouped_test.remove(grouped_test[i])
        grouped_train.remove(grouped_train[i])
        i -= 1
    i += 1
# print len(grouped_train), len(grouped_test)

# 误差总和记录, 首次训练模型记录
print "training..."
sum_error = []
first_train = []
first_error = []

for time in range(10):
    # 随机森林回归
    grouped_predict_relative = []
    for i in range(len(grouped_train)):
        max_depth = 20
        random_forest = RandomForestRegressor(max_depth=max_depth, random_state=random.randint(0, 10000000))
        random_forest.fit([x[2:3] for x in grouped_train[i].mr], [y[0:2] for y in grouped_train[i].mr])
        if time == 0:
            grouped_train[i].addrf(random_forest)
        grouped_predict_relative.append(random_forest.predict([x[2:3] for x in grouped_test[i].mr]))
    # print grouped_predict_relative[0]

    # 计算预测的原始位置
    grouped_predict_reality = []
    for i in range(len(grouped_train)):
        grouped_predict_reality.append([])
        for j in range(len(grouped_test[i].mr)):
            grouped_predict_reality[-1].append([grouped_predict_relative[i][j][0] + grouped_test[i].station[2],
                                                grouped_predict_relative[i][j][1] + grouped_test[i].station[3]])
    # print grouped_predict_reality[0]

    # 计算预测误差
    grouped_error = []
    for i in range(len(grouped_test)):
        grouped_error.append([])
        for j in range(len(grouped_test[i].mr)):
            grouped_error[-1].append(np.sqrt(pow(grouped_predict_reality[i][j][0] - grouped_test[i].mr[j][0], 2) +
                                             pow(grouped_predict_reality[i][j][1] - grouped_test[i].mr[j][1], 2)))
            # grouped_error[-1].sort()
    # print grouped_error[0]

    # 计算误差总和
    if time == 0:
        sum_error = np.array(grouped_error)
        first_train = np.array(grouped_predict_reality)
        first_error = np.array(grouped_error)
    else:
        for i in range(len(sum_error)):
            for j in range(len(sum_error[i])):
                sum_error[i][j] += grouped_error[i][j]

# 求平均误差并输出到csv
print "printing average error of 10 predicts..."
for i in range(len(grouped_test)):
    filename = 'predict/error_' + str(i) + '_' + str(len(grouped_train[i].mr)) + 'to' + str(
        len(grouped_test[i].mr)) + '_' + '.csv'
    np.savetxt(filename, np.sort(np.array([data / 10 for data in sum_error[i]])))

# 交叉预测
print "predicting by cross method..."
resultset = []
cross_error = []
for i in range(len(grouped_train)):
    resultset.append([])
    cross_error.append([])
    for j in range(len(grouped_train)):
        resultset[i].append([])
        if not j == i:
            relative = grouped_train[j].model.predict([x[2:3] for x in grouped_test[i].mr])
            reality = relative[:]
            for row in reality:
                row[0] += grouped_test[i].station[2]
                row[1] += grouped_test[i].station[3]
                resultset[i][j].append(row[0])
                resultset[i][j].append(row[1])
            error = []
            for k in range(len(grouped_test[i].mr)):
                error.append(np.sqrt(pow(reality[k][0] - grouped_test[i].mr[k][0], 2) +
                                     pow(reality[k][1] - grouped_test[i].mr[k][1], 2)))
            cross_error[i].append(error)
        else:
            for row in first_train[i]:
                resultset[i][j].append(row[0])
                resultset[i][j].append(row[1])
            cross_error[i].append(first_error[i])
# print resultset[0][0]

# 求NearestNeighbors
print "calculating nearest neighbors..."
nearest = []
nbrs = NearestNeighbors(n_neighbors=2)
for i in range(len(grouped_train)):
    nbrs.fit(np.array(resultset[i]))
    distance, index = nbrs.kneighbors(np.array(resultset[i][i]).reshape(1, -1))
    nearest.append([distance[0][1], index[0][1]])
# print nearest

# 交叉预测中最接近原始模型的误差，输出csv
print "printing errors in cross method..."
for i in range(len(grouped_test)):
    filename = 'cross/error_' + str(i) + '_by_' + str(nearest[i][1]) + '.csv'
    np.savetxt(filename, np.sort(np.array([data for data in cross_error[i][nearest[i][1]]])))
