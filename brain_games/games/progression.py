from random import randint
import secrets


RULES = "What number is missing in the progression?"


# создает арифметическую прогрессию
def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(str(current_element))
    return progression


# выбирает случайным образом параметры прогрессии
def generate_round():
    start = secrets.randbelow(20) + 1
    step = secrets.randbelow(10) + 1
    length = secrets.randbelow(6) + 5 

    # создается прогрессия на основе этих параметров
    progression = generate_progression(start, step, length)
    # выбирается случайный индекс
    hidden_index = secrets.randbelow(length)
    # число которое будет скрыто
    correct_answer = progression[hidden_index]
    # заменяем hide_index на ".."
    progression[hidden_index] = ".."
    question = " ".join(progression)

    return question, str(correct_answer)