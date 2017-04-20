"""
    Created by AMXPC on 2017/4/19.
"""

import pandas as pd
import random

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split


def rfr(x, y, r):
    max_depth = 15
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=r)

    random_forest = RandomForestRegressor(max_depth=max_depth, random_state=random.randint(1, 200))
    random_forest.fit(x_train, y_train)
    predict = random_forest.predict(x_test)

    print "RF Regressor score = %.2f" % random_forest.score(x_test, y_test)
    pd.DataFrame(predict).to_csv("rfr_predict.csv")
    return predict, y_test


def rfc(x, y, r):
    max_depth = 2
    while max_depth < 100:
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=r)

        random_forest = RandomForestClassifier(max_depth=max_depth, random_state=random.randint(1, 200))
        random_forest.fit(x_train, y_train)
        predict = random_forest.predict(x_test)

        print "RF Classifier score = %.2f" % random_forest.score(x_test, y_test)
    # pd.DataFrame(predict).to_csv("rfc_predict.csv")
        max_depth += 1
    # return predict, y_test
