"""
    Created by AMXPC on 2017/4/19.
"""

import pandas as pd

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split


def rfr(x, y):
    max_depth = 8
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=4)

    random_forest = RandomForestRegressor(max_depth=max_depth, random_state=3)
    random_forest.fit(x_train, y_train)
    predict = random_forest.predict(x_test)

    print "RF Regressor score = %.2f" % random_forest.score(x_test, y_test)
    pd.DataFrame(predict).to_csv("rfr_predict.csv")
    return predict, y_test


def rfc(x, y):
    max_depth = 20
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=4)

    random_forest = RandomForestClassifier(max_depth=max_depth, random_state=3)
    random_forest.fit(x_train, y_train)
    predict = random_forest.predict(x_test)

    print "RF Classifier score = %.2f" % random_forest.score(x_test, y_test)
    pd.DataFrame(predict).to_csv("rfc_predict.csv")
    return predict, y_test
