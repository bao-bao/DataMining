import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans


def kmeans(x, metric='hamming'):
    best_silhouette = -1
    best_clusters = 0
    cluster_silhouette = np.zeros((50, 2), dtype=int)

    for clusters in range(22, 23, 1):
        print 'Begin KMeans for cluster = %d' % clusters
        # do KMeans and calculate silhouette
        clt = KMeans(n_clusters=clusters)
        clt.fit(x)
        silhouette = metrics.silhouette_score(x, clt.labels_, metric=metric)

        # make map for (n_cluster, silhouette)
        cluster_silhouette[clusters][0] = clusters
        cluster_silhouette[clusters][1] = silhouette

        # get best n_clusters in KMeans
        if silhouette > best_silhouette:
            best_silhouette = silhouette
            best_clusters = clusters

    # out best cluster result to csv
    best_kmeans = KMeans(n_clusters=best_clusters)
    best_kmeans.fit(x)

    print best_clusters, best_silhouette

    return best_clusters, best_silhouette, best_kmeans.labels_
