import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import DBSCAN


def dbscan(x, min_eps, max_eps, delta):
    eps = min_eps
    best_eps = min_eps
    best_silhouette = -1
    eps_list = np.array([], dtype=float)
    silhouettes = np.array([], dtype=float)

    while eps < max_eps:
        print 'begin dbscan for eps = %f' % eps
        clf = DBSCAN(eps=eps, min_samples=15).fit(x)
        silhouette = metrics.silhouette_score(x, clf.labels_)

        if best_silhouette < silhouette:
            best_silhouette = silhouette
            best_eps = eps

        print 'For eps = %f, silhouette = %f' % (eps, silhouette)
        silhouettes = np.append(silhouettes, silhouette)
        eps_list = np.append(eps_list, eps)
        eps += delta

#    plt.plot(eps_list, silhouettes, 'b*')
#    plt.plot(eps_list, silhouettes, 'r')
#    plt.xlabel('eps')
#    plt.ylabel('silhouette')
#    plt.show()

    best_clf = DBSCAN(best_eps, min_samples=15).fit(x)
    np.savetxt('DbScanBest.csv', best_clf.labels_)
    np.savetxt('DbScanCenter.csv', best_clf.core_sample_indices_)
    print best_clf

    print 'Best eps = %f, silhouette = %f' % (best_eps, best_silhouette)
    save = pd.DataFrame({'eps': eps_list, 'silhouette': silhouettes})
    save.to_csv('DbscanOutput.csv')
#    return clf.labels_
