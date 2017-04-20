"""
    Created by AMXPC on 2017/4/19.
"""

import pandas as pd
import numpy as np
import ReadData
import RandomForest


def RFRoffset(x, y):
    predict, real = RandomForest.rfr(x, y)
    size = predict.shape[0]
    distance = np.zeros(4000)
    for row in xrange(size):
        print predict[row], real[row]
        distance[row] = 3


def RFCoffset(x, y):
    predict, real = RandomForest.rfc(x, y)


if __name__ == '__main__':
    data, target, grid = ReadData.readcsv("data/new4gtest.csv")
    # RandomForest.rfr(data, target)
    # RandomForest.rfc(data, grid)
    RFRoffset(data, target)
    # RFCoffset(data, grid)
