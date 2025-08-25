import secrets

# правила
RULES = "What is the result of the expression?"

# доступные операции
OPERATIONS = ['+', '-', '*']


# выполняет математическую операцию
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:  
        return num1 * num2


# генерация чисел, выбор операции, вопрос, вычисление ответа, возврат результата
def generate_round():
    num1 = secrets.randbelow(50) + 1
    num2 = secrets.randbelow(50) + 1
    operation = secrets.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)
    return question, str(correct_answer)