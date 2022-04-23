""" descriptive statistics
    continuous distributions """

from statistics import mean, median, mode, stdev, pstdev
from random import *

print(mean([50, 52, 53]))
print(median([50, 52, 53]))
print(median([51, 50, 52, 53]))
print(mode([51, 50, 52, 53, 51, 51]))
# # median: for unbalance distributions
print(stdev([51, 50, 52, 53, 51, 51]))
print(pstdev([51, 50, 52, 53, 51, 51]))

print(triangular(1000,1100))


print('triangular:')
data = [triangular(1000,1100) for i in range(1000)]
print(mean(data))
print(stdev(data))

print('uniform:')

data = [uniform(1000,1100) for i in range(1000)]
print(mean(data))
print(stdev(data))

print('gaussian:')

data = [gauss(100,15) for i in range(1000)]
print(mean(data))
print(stdev(data))

print('expovariate:')

data = [expovariate(20) for i in range(1000)]
print(mean(data))
print(stdev(data))

