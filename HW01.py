import queue
import time
import random


class Request:
    def __init__(self, request_id, description):
        self.request_id = request_id
        self.description = description


def generate_request(request_queue):
    # Генеруємо унікальний ідентифікатор заявки
    request_id = random.randint(1, 99999)
    description = f"Заявка {request_id}: Приклад опису заявки"
    new_request = Request(request_id, description)
    request_queue.put(new_request)
    print(f"Згенеровано нову заявку: {description}")


def process_request(request_queue):
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка заявки {request.request_id}: {request.description}")
        # Імітуємо час обробки
        time.sleep(random.uniform(0.5, 2))
        print(f"Заявку {request.request_id} успішно оброблено.")
    else:
        print("Черга заявок порожня.")


def main():
    request_queue = queue.Queue()

    while True:
        print("\nОпції:")
        print("1. Згенерувати нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")
        choice = input("Введіть номер опції: ")

        if choice == "1":
            generate_request(request_queue)
        elif choice == "2":
            process_request(request_queue)
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть 1, 2 або 3.")


if __name__ == "__main__":
    main()
