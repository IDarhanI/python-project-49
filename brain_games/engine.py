from brain_games.cli import welcome_user


def run_engine(game):
    name = welcome_user()
    print(game.RULES)


    for _ in range(3):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = input("Your answer: ").lower().strip()


        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("correct!")

    print(f"Congratulations, {name}!")