"""
    Created by AMXPC on 2017/3/29.
"""

import Kmeans
import DBScan
import GaussianMixture
from Util import *

matrix = ReadTraj_1000_SH_UTM.read()
# kmeans = Kmeans.kmeans(matrix)
gm = GaussianMixture.gaussian_mixture(matrix)
# dbscan = DBScan.dbscan(matrix, 15, 19, 0.5)
