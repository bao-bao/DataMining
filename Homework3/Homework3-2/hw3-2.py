"""
    Created by AMXPC on 2017/4/27.
"""
import ReadData

if __name__ == '__main__':
    dic = ReadData.readcsv_withtime("../data/new4gtrain.csv")
    dic = ReadData.readcsv_notime("../data/new4gtrain.csv")
