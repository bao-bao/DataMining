from sklearn.mixture import gaussian_mixture


def gaussianMixture(X):
    gm = gaussian_mixture.GaussianMixture()
    gm.fit(X)

    print gm.covariances_
