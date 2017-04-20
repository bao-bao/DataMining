"""
    Created by AMXPC on 2017/4/19.
"""
import time
import pandas as pd
import numpy as np


def readcsv(x):
    start = time.time()

    size = 20000

    data_ = np.full((size, 18), -999, dtype=float)
    target_ = np.full((size, 2), -999, dtype=float)
    grid_ = np.zeros(size, dtype=int)

    dataframe = pd.read_csv(x)

    for index, row in dataframe.iterrows():
        if index % 4 == 1 and index / 4 < 20000:
            i = 0
            while i < 6:
                data_[index / 4][i * 3] = row[i * 6 + 11]
                data_[index / 4][i * 3 + 1] = row[i * 6 + 12]
                data_[index / 4][i * 3 + 2] = row[i * 6 + 14] - row[i * 6 + 13]
                i += 1
            target_[index / 4][0] = row[9]
            target_[index / 4][1] = row[10]
            grid_[index / 4] = row[47]

    end = time.time()
    print "Read data in %.2fs" % (end - start)

    return data_, target_, grid_
