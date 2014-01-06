from operator import add
from operator import mul
from operator import sub
from operator import truediv

DIFFICULTY_OPERATIONS = {
    1:set([add]),
    2:set([sub]),
    3:set([add, sub]),
    4:set([mul]),
    5:set([truediv]),
    6:set([mul, truediv])
}

OPERAND_STRINGS = {
    add:"+",
    sub:"-",
    mul:"*",
    truediv:"/"
}

DIFFICULTY_RANGE = {
    1:100,
    2:100,
    3:100,
    4:10,
    5:10,
    6:10
}
