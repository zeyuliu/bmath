import random

from constants import DIFFICULTY_OPERATIONS

class Problem(object):
    """
    A Problem object represents a single problem.
    Contains a question, difficulty
    """

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.operands = DIFFICULTY_OPERATIONS.get(level, None)
        self.attempts = 0

    def generate_question(self):
        operand = random.sample(self.operands, 1)
        arg1 = random.randint

