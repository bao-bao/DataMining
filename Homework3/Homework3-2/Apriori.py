# coding=utf-8
"""
    A sample for Apriori algorithm
    ===============================================================
    *** dataset: dictionary of transactions
    *** minSupport: minimum support number rather than percentage
"""
import ReadData


def apriori(dataSet, minSupport=1):
    C1 = init_c1(dataSet)
    F1, supdata = scan(dataSet, C1, minSupport)
    F = [F1]
    print "iter = 1, candidate set length = %d" % len(F1)
    k = 2

    while len(F[k - 2]) > 0:
        Ck = candidategen(F[k - 2], k)
        Fk, supK = scan(dataSet, Ck, minSupport)
        print "F appending..."
        F.append(Fk)
        print "support data updating..."
        supdata.update(supK)
        print "iter = %d, candidate set length = %d" % (k, len(Fk))
        k += 1

    return F, supdata


def init_c1(dataset):
    items = list()
    for key, value in dataset.items():
        for item in value:
            if [item] not in items:
                items.append([item])
    items.sort()

    c1 = [frozenset(x) for x in items]

    # print c1
    return c1  # 候选集C1


def scan(dataset, ck, support):
    c = dict()
    for key, value in dataset.items():
        for candidate in ck:
            if candidate.issubset(value):
                c[candidate] = c.get(candidate, 0) + 1

    fk = list()
    supportdata = dict()
    for key in c:
        if c[key] >= support:
            fk.append(key)
            supportdata[key] = c[key]

    # print supportdata
    return fk, supportdata


def candidategen(fk, k):
    nextck = list()

    for i in xrange(len(fk) - 1):
        for j in xrange(i + 1, len(fk)):
            if len(fk[i] & fk[j]) == k - 2:    # 交集大小为k-2，取其并集作为下一步候选集元素
                nextck.append(fk[i] | fk[j])

    print "reducing Ck+1..."
    # print list(set(nextck))
    return list(set(nextck))

if __name__ == '__main__':
    data = ReadData.readcsv_notime("../data/new4gtrain.csv")
    frequent, sup = apriori(dataSet=data, minSupport=2)
    print frequent[-1]
