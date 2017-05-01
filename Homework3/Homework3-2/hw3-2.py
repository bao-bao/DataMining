"""
    Created by AMXPC on 2017/4/27.
"""
import ReadData
import TestData
import Apriori
import FPGrowth
import time

if __name__ == '__main__':
    # dic = ReadData.readcsv_notime("../data/new4gtrain.csv")
    dic = TestData.gettest()

    start = time.time()
    Afrequent, sup = Apriori.apriori(dataSet=dic, minSupport=2)
    end = time.time()
    ATime = end - start

    start = time.time()
    Ffrequent = FPGrowth.FPgrowth(dataSet=dic, minsupport=2)
    end = time.time()
    FTime = end - start

    print "Apriori:  time %.3fs    FrequentSet: %s" % (ATime, Afrequent)
    print "FPGrowth: time %.3fs    FrequentSet: %s" % (FTime, Ffrequent)

    # dic = ReadData.readcsv_withtime("../data/new4gtrain.csv")
