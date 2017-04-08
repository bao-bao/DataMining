import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans


def kmeans(x, metric='euclidean'):
    best_silhouette = -1
    best_clusters = 0
    clusters_list = np.array([], dtype=int)
    silhouettes_list = np.array([], dtype=float)

    for clusters in range(2, 30, 1):
        print 'Begin KMeans for cluster = %d' % clusters
        # do KMeans and calculate silhouette
        clt = KMeans(n_clusters=clusters, random_state=11)
        clt.fit_predict(x)
        silhouette = metrics.silhouette_score(x, clt.labels_, metric=metric)

        # make map for (n_cluster, silhouette)
        silhouettes_list = np.append(silhouettes_list, silhouette)
        clusters_list = np.append(clusters_list, clusters)

        # get best n_clusters in KMeans
        if silhouette > best_silhouette:
            best_silhouette = silhouette
            best_clusters = clusters

    save = pd.DataFrame({"cluster": clusters_list, "silhouette": silhouettes_list})
    save.to_csv('KMeansOutput.csv')

    # out best cluster result to csv
    best_kmeans = KMeans(n_clusters=best_clusters, random_state=1)
    best_kmeans.fit(x)
    np.savetxt("KMeansBest.csv", best_kmeans.labels_, delimiter=",")
    np.savetxt("KMeansCenter.csv", best_kmeans.cluster_centers_)

    print best_clusters, best_silhouette

    return best_clusters, best_silhouette, best_kmeans.labels_
