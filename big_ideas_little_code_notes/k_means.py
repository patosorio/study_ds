from collections import defaultdict
from typing import Iterable, Tuple
from math import fsum, sqrt
from pprint import pprint

""" Define data types """
Point = Tuple[int, ...]

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]


""" Calculate the average for all points"""

def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
    ' Euclidean distance function for multi-dimensinal data'
    return sqrt(fsum([(x - y)**2 for x, y in zip(p, q)]))

def assign_data(centroids, data):
    'Group the points by the closest centroid'
    d = defaultdict(list)
    for point in data:
        closest_centroid
        d[closest_centroid].append(point)
    return d

for point in points:
    print(point, dist(point, (9, 39, 20)))

