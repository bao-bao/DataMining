"""
    Created by AMXPC on 2017/4/27.
"""
import ReadData
import TestData
import Apriori
import FPgrowth

if __name__ == '__main__':
    # dic = ReadData.readcsv_withtime("../data/new4gtrain.csv")
    dic = TestData.gettest()
    frequent, sup = Apriori.apriori(dataSet=dic, minSupport=2)

    # dic = ReadData.readcsv_notime("../data/new4gtrain.csv")
