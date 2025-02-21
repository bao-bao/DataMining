"""
    Created by AMXPC on 2017/4/27.
"""
import ReadData
import TestData
import Apriori
import FPGrowth
import GSP
import time

if __name__ == '__main__':
    # dic = ReadData.readcsv_notime("../data/new4gtrain.csv")
    # dic_t = ReadData.readcsv_withtime("../data/new4gtrain.csv")
    dic = TestData.gettest()
    dic_t = TestData.getTimeTest()

    start = time.time()
    Afrequent, sup = Apriori.apriori(dataSet=dic, minSupport=2)
    end = time.time()
    ATime = end - start

    start = time.time()
    Ffrequent = FPGrowth.FPgrowth(dataSet=dic, minsupport=2)
    end = time.time()
    FTime = end - start

    start = time.time()
    Gfrequent = GSP.gsp(dataSet=dic_t, minsupport=2)
    end = time.time()
    GTime = end - start

    start = time.time()
    Sfrequent = GSP.gsp(dataSet=dic_t, minsupport=2)
    end = time.time()
    STime = end - start

    print dic
    print "Apriori:  time %.3fs    FrequentSet: %s" % (ATime, Afrequent)
    print "FPGrowth: time %.3fs    FrequentSet: %s" % (FTime, Ffrequent)
    print "GSP:      time %.3fs    FrequentSet: %s" % (GTime, Gfrequent)
    print "SPADE:    time %.3fs    FrequentSet: %s" % (STime, Gfrequent)
