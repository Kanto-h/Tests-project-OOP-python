from tests import TestManager, TrainingStrategy, ExamStrategy  # [ЗМІНА] Додали стратегії
from questions import QuestionFactory


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

                case _:
                    print("Помилка: Невірний вибір.")


    def _create_text_question(self, q_list):
        print("\n[Створення Текстового Питання]")
        data = {
            "text": input("Текст питання: "),
            "correct_answer": input("Правильна відповідь: "),
            "difficulty": int(input("Складність (1-5): "))
        }
        q = QuestionFactory.create_question("text", data)
        q_list.append(q)
        print("Питання додано через Фабрику!")

    def _create_one_choice(self, q_list):
        print("\n[Створення One Choice]")
        text = input("Текст питання: ")
        opts = [o.strip() for o in input("Варіанти (через кому): ").split(',')]

        for i, opt in enumerate(opts):
            print(f"{i + 1}. {opt}")

        correct_idx = int(input("Номер правильного варіанту: "))
        diff = int(input("Складність: "))

        data = {
            "text": text,
            "options": opts,
            "correct_idx": correct_idx,
            "difficulty": diff
        }

        q = QuestionFactory.create_question("one_choice", data)
        q_list.append(q)
        print("Питання додано через Фабрику!")

    def _create_multi_choice(self, q_list):
        print("\n[Створення Multi Choice]")
        text = input("Текст питання: ")
        opts = [o.strip() for o in input("Варіанти (через кому): ").split(',')]

        for i, opt in enumerate(opts):
            print(f"{i + 1}. {opt}")

        correct_str = input("Номери правильних (через кому): ")
        correct_indices = [int(x) for x in correct_str.split(',')]

        data = {
            "text": text,
            "options": opts,
            "correct_indices": correct_indices,
            "difficulty": 1  # Можна запитати у юзера
        }

        q = QuestionFactory.create_question("multi_choice", data)
        q_list.append(q)

    def _create_order(self, q_list):
        print("\n[Створення Order]")
        text = input("Текст завдання: ")
        items = [i.strip() for i in input("Елементи (через кому): ").split(',')]

        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

        order_str = input("Правильна послідовність (через пробіл): ")
        correct_order = [int(x) for x in order_str.split()]

        data = {
            "text": text,
            "items": items,
            "correct_order": correct_order,
            "difficulty": 1
        }

        q = QuestionFactory.create_question("order", data)
        q_list.append(q)

    def _create_matching(self, q_list):
        print("\n[Створення Matching]")
        text = input("Текст завдання: ")
        left = input("Лівий стовпчик (через кому): ").split(',')
        right = input("Правий стовпчик (через кому): ").split(',')

        print("Введіть пари (наприклад 1-B, 2-A).")
        pairs_input = input("Пари: ").replace(' ', '').split(',')

        pairs_dict = {}
        for p in pairs_input:
            k, v = p.split('-')
            pairs_dict[k] = v.upper()

        data = {
            "text": text,
            "left": left,
            "right": right,
            "pairs": pairs_dict,
            "difficulty": 1
        }

        q = QuestionFactory.create_question("matching", data)
        q_list.append(q)


class Student(User):
    def __init__(self, login):
        super().__init__(login)

    def show_menu(self, question_list):
        if not question_list:
            print("Тестів немає. Попросіть адміна додати питання.")
            return

        print("\nОберіть режим тестування:")
        print("1. Тренування (з підказками)")
        print("2. Екзамен (суворий режим)")
        mode_choice = input("Ваш вибір: ")

        strategy = None
        match mode_choice:
            case "1":
                strategy = TrainingStrategy()
            case "2":
                strategy = ExamStrategy()
            case _:
                print("Невірний вибір. Вмикаємо режим тренування за замовчуванням.")
                strategy = TrainingStrategy()

        manager = TestManager(self.login, strategy)

        for q in question_list:
            manager.add_question(q)

        manager.run_test()