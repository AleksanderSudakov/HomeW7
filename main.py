# Написати декоратор для будь якої функції, що буде зберігати історію викликів функцій у файлі. Тобто всі функції що будуть задекоровані цим декоратором з кожним викликом мають записути у файл наступний рядок:
#
# {Function name} was called with args {args & kwargs} at {time} and return result {result}

import time


def decorator_example(accepted_function):

    def wrapper(*args, **kwargs):
        file_result = open("log", "a")

        result = accepted_function(*args, **kwargs)

        from datetime import datetime
        file_result.write(f"{accepted_function.__name__} was called with args {args} {kwargs} at {datetime.now().time()} and return result {result}" + "\n")

        return result

    return wrapper

@decorator_example
def add_two_number(k, c):
    return k + c

print(add_two_number(20, 30))