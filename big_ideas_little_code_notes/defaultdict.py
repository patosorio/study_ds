from collections import defaultdict
from pprint import pprint

d = {'raymond': 'red'}
e = defaultdict(lambda: 'black')
e['raymond'] = 'red'


m = [
    [10,20],
    [30,40],
    [50,60]
]

pprint(list(zip(*m)), width=15)
