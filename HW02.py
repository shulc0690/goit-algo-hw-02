from collections import deque


def is_palindrome(s):
    # Видаляємо пробіли та перетворюємо на рядок у нижньому регістрі
    s = s.replace(" ", "").lower()

    # Створюємо чергу (deque) з рядка
    char_queue = deque(s)

    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


example = [
    "Я несу гусеня",
    "Я несу щось дивне",
    "А роза упала на лапу Азора",
    "Роза впала на землю",
]
# Приклад використання
for input_string in example:
    if is_palindrome(input_string):
        print(f"'{input_string}' є паліндромом.")
    else:
        print(f"'{input_string}' не є паліндромом.")
