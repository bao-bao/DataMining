"""
    Created by AMXPC on 2017/4/19.
"""

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


def rfr(x, y):
    estimator = RandomForestRegressor(random_state=0, n_estimators=100)

