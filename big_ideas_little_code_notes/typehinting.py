from typing import *
from collections import OrderedDict, deque, namedtuple
import secrets

x = 10          # type : int


def f(x: int, y: Optional[int]=None) -> int:
    if y is None:
        y = 20
    return x + y

y = OrderedDict()          # type: OrderedDict

""" sequence : indexable and iterable """
def g(x: List[int]) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

g([10,20,30])
#g((11, 12, 13)) # expected a list

hts = [97.1, 102.5, 97.5]       # type : List[float]
person = ('Raymond', 5 * 12 + 11)   # type : Tuple[str, float]
info = ('Person', 'Course', 'Python', 'Raymond')    # type : Tuple[str, ...]

fifo = deque()              # type: deque

print(f'The answer is {x} today')

Point = namedtuple('Point', [('x', int), ('y', int)])



