import random
from operator import floordiv

from constants import DIFFICULTY_OPERATIONS
from constants import DIFFICULTY_RANGE
from constants import OPERAND_STRINGS

class Problem(object):
    """
    A Problem object represents a single problem.
    Contains a question, difficulty
    """

    def __init__(self, difficulty, num_range=0, negatives=False):
        #self.difficulty = floordiv(difficulty+1, 2)
        self.difficulty = difficulty
        self.negative = negatives
        self.operands = DIFFICULTY_OPERATIONS.get(self.difficulty)
        self._attempts = 0
        self.correct = False
        self.range = num_range or DIFFICULTY_RANGE.get(self.difficulty)
        self.generate_question()
        self.guesses = []

    def generate_question(self):
        self.operand = random.sample(self.operands, 1)[0]
        lowerbound = -1 * self.range if self.negative else 0
        self.arg1 = random.randint(lowerbound, self.range)
        self.arg2 = random.randint(lowerbound, self.range)
        self.solution = self.operand(self.arg1, self.arg2)

    def attempts(self):
        return self._attempts

    def solve(self, guess):
        self._attempts += 1
        self.guesses.append(guess)
        if self.solution == guess:
            self.correct = True
        else:
            self.correct = False
        return self.correct
        

    def __str__(self):
        return "%d %s %d" % (self.arg1, OPERAND_STRINGS.get(self.operand), self.arg2,)

    def __repr__(self):
        return str(self)
