from random import randint
import secrets


# правила
RULES = 'Aswer "yes" if given number is prime. Otherwise answer "no".'


# функция проверки на простое число
def is_prime(number):
    if number < 2:         
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # проверяем нечетные делители от 3 до квадратного корня из числа
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def generate_round():
    number = secrets.randbelow(100) + 1
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer