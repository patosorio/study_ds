from collections import Counter

d = {}
#d['dragons']

""" the traditional dictionary
if it has missing key
will raise a key error """

d = Counter()
d['dragons']
d['dragons'] += 6
print(d)