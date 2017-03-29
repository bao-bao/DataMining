from sklearn.cluster import DBSCAN


def DbScan(x):
    clf = DBSCAN(eps=0.3, min_samples=10).fit(x)
    return clf.labels_
