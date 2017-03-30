"""
    Created by AMXPC on 2017/3/29.
"""

import Kmeans
import DBScan
import GaussianMixture
from Util import *

matrix = ReadTraj_1000_SH_UTM.read()

kmeans = Kmeans.kmeans(matrix)
# gm = GaussianMixture.gaussianMixture(matrix)
# dbscan = DBScan.DbScan(matrix, 15, 25, 0.5)
