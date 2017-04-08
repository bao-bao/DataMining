import numpy as np

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

from sklearn.mixture import GaussianMixture
from sklearn.model_selection import StratifiedKFold
from sklearn.decomposition import PCA


def gaussian_mixture(m, x, n_components):
    pca = PCA(n_components=1000)
    data_ = pca.fit_transform(x)

    if m == 'kmeans':
        target_ = KMeans(n_clusters=2, random_state=11).fit_predict(data_)

    if m == 'dbscan':
        dbscan = DBSCAN(eps=20, min_samples=5).fit(data_)
        target_ = dbscan.labels_

    # Break up the dataset into non-overlapping training (75%) and testing
    # (25%) sets.
    skf = StratifiedKFold(n_splits=4)
    # Only take the first fold.
    train_index, test_index = next(iter(skf.split(data_, target_)))
    print train_index, test_index

    x_train = data_[train_index]
    y_train = target_[train_index]
    x_test = data_[test_index]
    y_test = target_[test_index]

    n_classes = len(np.unique(y_train))

    # Try GMMs using different types of covariances.
    estimators = dict((cov_type, GaussianMixture(n_components=n_components,
                                                 covariance_type=cov_type, max_iter=20, random_state=0))
                      for cov_type in ['spherical', 'diag', 'tied', 'full'])

    for index, (name, estimator) in enumerate(estimators.items()):
        # Since we have class labels for the training data, we can
        # initialize the GMM parameters in a supervised manner.
        estimator.means_init = np.array([x_train[y_train == i].mean(axis=0)
                                         for i in range(n_classes)])

        # Train the other parameters using the EM algorithm.
        estimator.fit(x_train)

        y_train_pred = estimator.predict(x_train)
        train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
        print 'Train accuracy: %.1f' % train_accuracy

        y_test_pred = estimator.predict(x_test)
        test_accuracy = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100
        print 'test accuracy: %.1f' % test_accuracy
