"""
    Created by AMXPC on 2017/4/19.
"""

import random
import numpy as np
import ReadData
import RandomForest


def RFRoffset(x, y):
    p, q = RandomForest.rfr(x, y, random.randint(1, 999))
    size = p.shape[0]
    distance_ = np.zeros(size)

    i = 0
    while i < 10:
        predict, real = RandomForest.rfr(x, y, random.randint(1, 999))
        for row in xrange(size):
            a = predict[row]
            b = real[row]
            distance_[row] += np.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2))
        i += 1

    print distance_[0]
    for row in xrange(distance_.shape[0]):
        distance_[row] /= 10
    np.savetxt("rfr_offset.csv", np.sort(distance_))
    print distance_[0]
    return np.sort(distance_), len(distance_)


def RFCoffset(x, y):
    p, q = RandomForest.rfc(x, y, random.randint(1, 999))
    size = p.shape[0]
    correct_ = np.zeros(10)

    i = 0
    while i < 10:
        correct = 0
        predict, real = RandomForest.rfc(x, y, random.randint(1, 999))
        for row in xrange(size):
            if predict[row] == real[row]:
                correct += 1
        correct_[i] = correct
        i += 1

    print correct_
    return correct_


if __name__ == '__main__':
    data, target, grid = ReadData.readcsv("data/new4gtrain.csv")
    # RandomForest.rfr(data, target)
    # RandomForest.rfc(data, grid)
    RFRoffset(data, target)
    # RFCoffset(data, grid)
