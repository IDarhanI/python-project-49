from random import randint

from brain_games.cli import welcome_user


def is_even(num):
    return num % 2 == 0


def run_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").lower().strip()

        correct_answer = 'yes' if is_even(number) else 'no'

        if answer not in ('yes', 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
    
    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()


        
