from random import choice, randint

RULES = "What is the result of the expression?"
OPERATIONS = ['+', '-', '*']


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:  # '*'
        return num1 * num2


def generate_round():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operation = choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)
    return question, str(correct_answer)