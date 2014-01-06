from game import Game


def main():
    difficulty = prompt_difficulty()
    g = Game(difficulty)
    questions = prompt_num_questions()
    while questions > 0:
        g.generate_problem()
        g.prompt_problem()
        questions -= 1
    return




def prompt_difficulty():
    allowed_difficulty = False
    while not allowed_difficulty:
        try:
            difficulty = int(input("What difficulty problems would you like?\n\
1 - Addition\n\
2 - Subtraction\n\
3 - Addition & Subtraction\n\
4 - Multiplication\n\
5 - Division\n\
6 - Multiplication & Division\n"))
            allowed_difficulty = True
        except TypeError:
            pass
    return difficulty

def prompt_num_questions():
    allowed_number = False
    while not allowed_number:
        try:
            num_questions = int(input("How many problems would you like to do? "))
            allowed_number = True
        except TypeError:
            pass
    return num_questions
    
if __name__== "__main__":
    main()
