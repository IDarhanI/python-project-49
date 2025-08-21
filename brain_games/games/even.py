from random import randint

# правила
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# проверка на четность
def is_even(num):
    return num % 2 == 0


def generate_round():
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer


        
