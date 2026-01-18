from tests import TestManager
from questions import (
    TextQuestion, OneChoiceQuestion, MultiChoiceQuestion,
    OrderQuestion, MatchingQuestion
)

class User:
    def __init__(self, login):
        self.login = login

    def show_menu(self, context_data):
        raise NotImplementedError("Метод show_menu має бути реалізований")

class Admin(User):
    def __init__(self, login="admin"):
        super().__init__(login)

    def show_menu(self, question_list):
        while True:
            print(f"\n--- ПАНЕЛЬ АДМІНІСТРАТОРА ({self.login}) ---")
            print("1. Додати просте текстове питання")
            print("2. Додати питання з вибором (один)")
            print("3. Додати питання з вибором (декілька)")
            print("4. Додати питання на послідовність")
            print("5. Додати питання на відповідність")
            print("6. Показати всі питання")
            print("0. Вихід (Зберегти та почати тест)")

            choice = input("Ваш вибір: ")

            match choice:
                case "0":
                    print("[Система]: Збереження змін та вихід з панелі адміна...")
                    break
                case "1":
                    self._create_text_question(question_list)
                case "2":
                    self._create_one_choice(question_list)
                case "3":
                    self._create_multi_choice(question_list)
                case "4":
                    self._create_order(question_list)
                case "5":
                    self._create_matching(question_list)
                case "6":
                    print(f"\n--- СПИСОК ПИТАНЬ У БАЗІ ({len(question_list)}) ---")
                    if not question_list:
                        print("База поки що порожня.")
                    else:
                        for i, q in enumerate(question_list, 1):
                            type_name = q.__class__.__name__
                            print(f"{i}. [{type_name}] {q.text} (Складність: {q.difficulty})")

                case _:  # Аналог default у C++
                    print("Помилка: Невірний вибір. Будь ласка, введіть цифру від 0 до 6.")


    def _create_text_question(self, q_list):
        print("\n[Створення Текстового Питання]")
        text = input("Текст питання: ")
        ans = input("Правильна відповідь: ")
        diff = int(input("Складність (1-5): "))
        q = TextQuestion(text, ans, diff)
        q_list.append(q)
        print("Питання додано!")

    def _create_one_choice(self, q_list):
        print("\n[Створення One Choice]")
        text = input("Текст питання: ")
        opts = input("Варіанти (через кому, напр: Київ,Львів,Одеса): ").split(',')
        opts = [o.strip() for o in opts]

        for i, opt in enumerate(opts):
            print(f"{i + 1}. {opt}")

        correct = int(input("Номер правильного варіанту: "))
        diff = int(input("Складність: "))

        q = OneChoiceQuestion(text, opts, correct, diff)
        q_list.append(q)
        print("Питання додано!")

    def _create_multi_choice(self, q_list):
        print("\n[Створення Multi Choice]")
        text = input("Текст питання: ")
        opts = input("Варіанти (через кому): ").split(',')
        opts = [o.strip() for o in opts]

        for i, opt in enumerate(opts):
            print(f"{i + 1}. {opt}")

        correct_str = input("Номери правильних (через кому, напр: 1,3): ")
        correct_indices = [int(x) for x in correct_str.split(',')]

        q = MultiChoiceQuestion(text, opts, correct_indices, 1)
        q_list.append(q)
        print("Питання додано!")

    def _create_order(self, q_list):
        print("\n[Створення Order]")
        text = input("Текст завдання: ")
        items = input("Елементи у ВИПАДКОВОМУ порядку (через кому): ").split(',')
        items = [i.strip() for i in items]

        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

        order_str = input("Правильна послідовність номерів (через пробіл, напр: 3 1 2): ")
        correct_order = [int(x) for x in order_str.split()]

        q = OrderQuestion(text, items, correct_order)
        q_list.append(q)

    def _create_matching(self, q_list):
        print("\n[Створення Matching]")
        text = input("Текст завдання: ")
        left = input("Лівий стовпчик (через кому): ").split(',')
        right = input("Правий стовпчик (через кому): ").split(',')

        print("Введіть пари (наприклад 1-B, 2-A).")
        print(f"Ліво: {[f'{i + 1}.{x}' for i, x in enumerate(left)]}")
        print(f"Право: {[f'{chr(65 + i)}.{x}' for i, x in enumerate(right)]}")

        pairs_input = input("Пари: ").replace(' ', '').split(',')
        pairs_dict = {}
        for p in pairs_input:
            k, v = p.split('-')
            pairs_dict[k] = v.upper()

        q = MatchingQuestion(text, left, right, pairs_dict)
        q_list.append(q)

class Student(User):
    def __init__(self, login):
        super().__init__(login)

    def show_menu(self, question_list):
        if not question_list:
            print("Тестів немає. Попросіть адміна додати питання.")
            return

        manager = TestManager(self.login)

        for q in question_list:
            manager.add_question(q)

        manager.run_test()