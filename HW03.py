from collections import deque


def check_delimiters(input_string):
    # Створюємо стек для відстеження відкритих розділювачів
    stack = []

    # Визначаємо відповідність відкритих та закритих розділювачів
    delimiter_map = {"(": ")", "[": "]", "{": "}"}

    # Перебираємо кожний символ у вхідному рядку
    for char in input_string:
        if char in delimiter_map:
            # Якщо це відкритий розділювач, додаємо його до стеку
            stack.append(char)
        elif char in delimiter_map.values():
            # Якщо це закритий розділювач, перевіряємо, чи він відповідає вершині стеку
            if not stack or delimiter_map[stack.pop()] != char:
                return "Несиметрично"

    # Якщо стек порожній, всі розділювачі відповідають один одному
    return "Симетрично" if not stack else "Несиметрично"


# Приклад використання
input_string1 = "( ){ 1 ( ){ }}"
input_string2 = "( 23 ( 2 - 3);"
input_string3 = "( 11 }"

print(f"'{input_string1}': {check_delimiters(input_string1)}")
print(f"'{input_string2}': {check_delimiters(input_string2)}")
print(f"'{input_string3}': {check_delimiters(input_string3)}")
