# coding=utf-8
"""
    Created by AMXPC on 2017/4/8.
"""
import math
import pandas as pd
import numpy as np
import ReadTraj_1000_SH_UTM as rt

# for convenient only
sin = math.sin
cos = math.cos
tan = math.tan
sqrt = math.sqrt
radians = math.radians
degrees = math.degrees
pi = math.pi

a = 6378137
b = 6356752.3142451
lon0 = 123


def UTM2LL_USGS(x, y):
    """
    ** x 经过UTM投影后的经度方向的坐标，也就是UTMEasting
    ** y 经过UTM投影后的纬度方向的坐标，也就是UTMNorthing
    ** lon0 中央经度线
    ---------------------------------------------
    ** Output:(lat, lon)
    ** lat 维度（角度为单位）
    ** lon 经度（角度为单位）
    ---------------------------------------------
    ** 功能描述：UTM坐标转换为经纬度坐标
    """

    x = 500000 - x
    k0 = 0.9996
    e = sqrt(1 - b ** 2 / a ** 2)
    # calculate the meridional arc
    M = y / k0
    # calculate footprint latitude
    mu = M / (a * (1 - e ** 2 / 4 - 3 * e ** 4 / 64 - 5 * e ** 6 / 256))
    e1 = (1 - (1 - e ** 2) ** (1.0 / 2)) / (1 + (1 - e ** 2) ** (1.0 / 2))

    J1 = (3 * e1 / 2 - 27 * e1 ** 3 / 32)
    J2 = (21 * e1 ** 2 / 16 - 55 * e1 ** 4 / 32)
    J3 = (151 * e1 ** 3 / 96)
    J4 = (1097 * e1 ** 4 / 512)
    fp = mu + J1 * sin(2 * mu) + J2 * sin(4 * mu) + J3 * sin(6 * mu) + J4 * sin(8 * mu)

    # Calculate Latitude and Longitude

    e2 = e ** 2 / (1 - e ** 2)
    C1 = e2 * cos(fp) ** 2
    T1 = tan(fp) ** 2
    R1 = a * (1 - e ** 2) / (1 - (e * sin(fp)) ** 2) ** (3.0 / 2)  # This is the same as rho in the forward conversion formulas above, but calculated for fp instead of lat.
    N1 = a / (1 - (e * sin(fp)) ** 2) ** (1.0 / 2)  # This is the same as nu in the forward conversion formulas above, but calculated for fp instead of lat.
    D = x / (N1 * k0)

    Q1 = N1 * tan(fp) / R1
    Q2 = (D ** 2 / 2)
    Q3 = (5 + 3 * T1 + 10 * C1 - 4 * C1 ** 2 - 9 * e2) * D ** 4 / 24
    Q4 = (61 + 90 * T1 + 298 * C1 + 45 * T1 ** 2 - 3 * C1 ** 2 - 252 * e2) * D ** 6 / 720
    lat = degrees(fp - Q1 * (Q2 - Q3 + Q4))

    Q5 = D
    Q6 = (1 + 2 * T1 + C1) * D ** 3 / 6
    Q7 = (5 - 2 * C1 + 28 * T1 - 3 * C1 ** 2 + 8 * e2 + 24 * T1 ** 2) * D ** 5 / 120
    lon = lon0 - degrees((Q5 - Q6 + Q7) / cos(fp))
    return lat, lon

if __name__ == '__main__':
    tid = np.array([], dtype=int)
    lat = np.array([], dtype=float)
    lon = np.array([], dtype=float)
    data = pd.read_csv("Traj_1000_SH_UTM")
    for index, row in data.iterrows():
        (lat_, lon_) = UTM2LL_USGS(row[2], row[3])
        tid = np.append(tid, row[0])
        lat = np.append(lat, lat_)
        lon = np.append(lon, lon_)

    save = pd.DataFrame({"lon": lon, "lat": lat, "tid": tid})
    save.to_csv('TraceLL.csv')

