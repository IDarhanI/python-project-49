from brain_games.cli import welcome_user


# получаем имя пользователя и выводим правила
def run_engine(game):
    name = welcome_user()
    print(game.RULES)


# задаем цикл на 3 раунда
    for _ in range(3):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        
        # проверка ответа
        answer = input("Your answer: ").lower().strip()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("correct!")

    print(f"Congratulations, {name}!")