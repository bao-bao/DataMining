import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import DBSCAN


def DbScan(x, min_eps, max_eps, delta):
    eps = min_eps
    best_eps = min_eps
    best_silhouette = -1
    eps_list = np.array([], dtype=float)
    silhouettes = np.array([], dtype=float)

    while eps < max_eps:
        print 'begin dbscan for eps = %f' % eps
        clf = DBSCAN(eps=eps, min_samples=10).fit(x)
        silhouette = metrics.silhouette_score(x, clf.labels_)

        if best_silhouette < silhouette:
            best_silhouette = silhouette
            best_eps = eps

        print 'For eps = %f, silhouette = %f' % (eps, silhouette)
        silhouettes = np.append(silhouettes, silhouette)
        eps_list = np.append(eps_list, eps)
        eps += delta

    plt.plot(eps_list, silhouettes, 'b*')
    plt.plot(eps_list, silhouettes, 'r')
    plt.xlabel('eps')
    plt.ylabel('silhouette')
    plt.show()

    print 'Best eps = %f, silhouette = %f' %(best_eps, best_silhouette)

#    return clf.labels_
