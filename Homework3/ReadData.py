"""
    Created by AMXPC on 2017/4/19.
"""
import time
import pandas as pd
import numpy as np


def readcsv(x):
    dataframe = pd.read_csv(x)
    size = dataframe.shape[0]

    data_ = np.full((size, 18), -999, dtype=float)
    target_ = np.full((size, 2), -999, dtype=float)
    grid_ = np.zeros(size, dtype=int)

    for index, row in dataframe.iterrows():
        i = 0
        while i < 6:
            data_[index][i * 3] = row[i * 6 + 11]
            data_[index][i * 3 + 1] = row[i * 6 + 12]
            data_[index][i * 3 + 2] = row[i * 6 + 14] - row[i * 6 + 13]
            i += 1
        target_[index][0] = row[9]
        target_[index][1] = row[10]
        grid_[index] = row[47]

    print "%.2f lines read from %s" % (size, x)

    return data_, target_, grid_
