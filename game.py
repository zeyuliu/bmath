from problem import Problem

class Game(object):
    
    def __init__(self, difficulty, num_range=0):
        self.difficulty = difficulty
        self.range = num_range
        self.problems = []
        self.curr_problem = None

    def generate_problem(self):
        p = Problem(self.difficulty, self.range)
        self.problems.append(p)
        self.curr_problem = p
        return p

    def prompt_problem(self):
        correct = False
        while not correct:
            guess = input("What is %s? " % (str(self.curr_problem),))
            try:
                guess = int(guess)
                correct = self.curr_problem.solve(guess)
            except TypeError:
                pass
        return self.curr_problem.attempts()

    
