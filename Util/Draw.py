"""
    Created by AMXPC on 2017/4/8.
"""

import pandas as pd


def draw(i):
    html = open('map.html', 'w+')
    script = ['< script type = "text/javascript" >\n',
              'var map = new BMap.Map("container");\n',
              'map.centerAndZoom(new BMap.Point(118.454, 32.955), 6);\n',
              'map.enableScrollWheelZoom();\n',
              'var polyline = new BMap.Polyline([\n']

    data = pd.read_csv("TraceLL.csv")
    for index, row in data.iterrows():
        if row[3] == i:
            point = 'new BMap.Point(' + str(row[2]) + ',' + str(row[1]) + '),\n'
            list.append(script, point)

    list.append(script, '], {strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});\n')
    list.append(script, 'map.addOverlay(polyline);\n')
    list.append(script, '</script>')

    html.writelines(script)


if __name__ == '__main__':
    draw(395)
