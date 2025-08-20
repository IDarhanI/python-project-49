from random import randint, choice


RULES = "What number is missing in the progression?"


def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index + step
        progression.append(str(current_element))
    return progression


def generate_round():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint (5, 10)


    progression = generate_progression(start, step, length)


    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."
    question = " ".join(progression)


    return question, correct_answer