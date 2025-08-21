from random import randint

RULES = "What number is missing in the progression?"

#создает арифметическую прогрессию
def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(str(current_element))
    return progression

#выбирает случайным образом параметры прогрессии
def generate_round():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)

    # создается прогрессия на основе этих параметров
    progression = generate_progression(start, step, length)
    #выбирается случайный индекс
    hidden_index = randint(0, length - 1)
    #число которое будет скрыто
    correct_answer = progression[hidden_index]
    #заменяем hide_index на ".."
    progression[hidden_index] = ".."
    question = " ".join(progression)

    return question, correct_answer