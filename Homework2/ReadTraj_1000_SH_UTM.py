import pandas as pd
import numpy as np


def read():
    data = pd.read_csv("Traj_1000_SH_UTM")

    temparray = np.zeros((840 * 760))
    matrix = np.zeros((1000, 44107))

    for index, row in data.iterrows():
        temparray[int((row[2] - 346000) / 20) * 760 + int((row[3] - 3448600) / 20)] = 1

    i = 0
    count = 0

    while i < 638400:
        if temparray[i] == 1:
            temparray[i] = count
            count += 1
        i += 1

    tid = 0
    while tid < 1000:
        trace = data.loc[(data['Tid'] == tid + 1), ['Time', 'X', 'Y']]
        for index, row in trace.iterrows():
            matrix[tid][temparray[int((row[1] - 346000) / 20) * 760 + int((row[2] - 3448600) / 20)]] = 1
        tid += 1

    save = pd.DataFrame(matrix, dtype=int)
    return save
