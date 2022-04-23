from random import choice, choices, sample, shuffle
from collections import Counter

""" choice : pick a single choice out of a list """

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

print('Choice:')
print(choice(outcomes))

""" sampling with replacement"""

print('Multiple Choices:')
print(choices(outcomes, k=10))

print('Counter:')
print(Counter(choices(outcomes, k=10000)))

""" we can supply some weigths to the outcome with choiceS """

print(Counter(choices(outcomes, [5, 4, 3, 2, 1], k=10000)))

print(shuffle(outcomes))

""" sampling without replacement """

print(sample(outcomes, k=4))

# lottery!

lottery = sample(range(1, 57), k=6)
print(lottery)

# choice and shuffle is a special case of a sample,
print(sample(outcomes, k=1)[0])

print(shuffle(outcomes)) ; outcomes

sample(outcomes, k=len(outcomes))

