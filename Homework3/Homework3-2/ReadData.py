"""
    Created by AMXPC on 2017/4/27.
"""
import pandas as pd


def readcsv_notime(x):
    dataframe = pd.read_csv(x)
    dic = dict()

    for index, row in dataframe.iterrows():
        if row[1] not in dic:
            dic[row[1]] = []
        if row[47] not in dic[row[1]]:
            dic[row[1]].append(row[47])

    # print dic
    return dic


def readcsv_withtime(x):
    dataframe = pd.read_csv(x)
    dic = dict()
    time = ''

    for index, row in dataframe.iterrows():
        if row[1] not in dic:
            dic[row[1]] = []
        if row[0] != time:
            dic[row[1]].append([])
        if row[47] not in dic[row[1]][-1]:
            dic[row[1]][-1].append(row[47])
        time = row[0]

    # print dic
    return dic
