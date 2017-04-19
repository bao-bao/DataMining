"""
    Created by AMXPC on 2017/3/29.
"""

import Kmeans
import DBScan
import GaussianMixture
import ReadTraj_1000_SH_UTM

matrix = ReadTraj_1000_SH_UTM.read()
# kmeans = Kmeans.kmeans(matrix)
# dbscan = DBScan.dbscan(matrix, 12, 19, 0.5)
gm = GaussianMixture.gaussian_mixture('dbscan', matrix, 2)
