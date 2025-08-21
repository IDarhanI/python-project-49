from random import randint

#правила
RULES = "Find the greatest common divisor of given numbers."


#используем алгоритм Евклида
def calculeate_gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a



def generate_round():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = calculeate_gcd(a, b)
    return question, str(correct_answer)