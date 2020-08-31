from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def isInside(point,area):
    res = area.contains(point)
    return res
    # point = Point(0.5, 0.5)
    # polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    # print(polygon.contains(point)
if __name__ == '__main__':
    point = Point(1,1)
    area = Polygon([(0,0),(0,3),(2,1),(2,0)])
    print(isInside(point,area))
