from operator import add
from operator import mul
from operator import sub
from operator import truediv

DIFFICULTY_OPERATIONS = dict(
    1=set([add]),
    2=set([sub]),
    3=set([add, sub]),
    4=set([mul]),
    5=set([truediv]),
    6=set([mul, truediv])
)
