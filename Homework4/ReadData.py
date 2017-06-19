# coding=utf-8
"""
    Created by AMXPC on 2017/6/17.
"""
import pandas as pd
import numpy as np


def readpt(x):
    # 原始数据
    dataframe = pd.read_csv(x)
    size = dataframe.shape[0]
    # 需要的数据列
    data_ = np.full((size, 5), 0, dtype=float)
    i = 0
    for index, row in dataframe.iterrows():
        # 空值判断
        if np.isnan(row[10]) or np.isnan(row[11]) or np.isnan(row[12]) or np.isnan(row[13]) or \
                np.isnan(row[14]) or np.isnan(row[15]):
            continue
        data_[i][0] = row[12]
        data_[i][1] = row[13]
        data_[i][2] = row[10]
        data_[i][3] = row[11]
        data_[i][4] = row[15] - row[14]
        i += 1
    # 去除多余行
    data_ = data_[~(data_ == 0).any(1)]

    print "%d/%d lines read from %s" % (data_.shape[0], size, x)

    np.savetxt('2gte.csv', data_, delimiter=',')
    return data_


def readgc_2g(x):
    # 原始数据
    dataframe = pd.read_csv(x)
    size = dataframe.shape[0]
    # 需要的数据列
    data_ = np.full((size, 4), 0, dtype=float)
    i = 0
    for index, row in dataframe.iterrows():
        # 空值判断
        if np.isnan(row[5]) or np.isnan(row[6]) or np.isnan(row[13]) or np.isnan(row[14]):
            continue
        data_[i][0] = row[5]
        data_[i][1] = row[6]
        data_[i][2] = row[13]
        data_[i][3] = row[14]
        i += 1
    # 去除多余行
    data_ = data_[~(data_ == 0).any(1)]

    print "%d/%d lines read from %s" % (data_.shape[0], size, x)

    np.savetxt('2ggc.csv', data_, delimiter=',')
    return data_
