from random import randint
import secrets


# правила
RULES = "Find the greatest common divisor of given numbers."


# используем алгоритм Евклида
def calculeate_gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a


def generate_round():
    a = secrets.randbelow(100) + 1
    b = secrets.randbelow(100) + 1
    question = f"{a} {b}"
    correct_answer = calculeate_gcd(a, b)
    return question, str(correct_answer)