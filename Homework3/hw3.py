"""
    Created by AMXPC on 2017/4/19.
"""

import time
import ReadData
import RandomForest


def RandomForestRegressor():
    start_time = time.time()
    data, target, grid = ReadData.readcsv("data/new2gtrain.csv")
    RandomForest.rfr(data, target)
    stop_time = time.time()

    print "Simple use %.2f seconds" % (stop_time - start_time)


def RandomForestClassifier():
    start_time = time.time()
    data, target, grid = ReadData.readcsv("data/new2gtrain.csv")
    RandomForest.rfc(data, grid)
    stop_time = time.time()

    print "Simple use %.2f seconds" % (stop_time - start_time)


if __name__ == '__main__':
    # RandomForestRegressor()
    RandomForestClassifier()
