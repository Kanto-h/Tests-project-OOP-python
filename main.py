from admin import Admin, Student
from questions import TextQuestion, OneChoiceQuestion, MultiChoiceQuestion


def create_initial_data():
    demo_list = []

    q1 = TextQuestion("Столиця Франції?", "Париж", difficulty=1)

    q2 = OneChoiceQuestion("Скільки біт у байті?", ["4", "8", "16"], 2, difficulty=1)

    q3 = MultiChoiceQuestion("Що з цього фрукти?", ["Яблуко", "Картопля", "Груша"], [1, 3], difficulty=2)

    demo_list.extend([q1, q2, q3])
    return demo_list

def main():
    print("\n" + "=" * 40)
    print("      СИСТЕМА ТЕСТУВАННЯ (ЛР №3)      ")
    print("      Наслідування та Поліморфізм      ")
    print("=" * 40)

    question_database = create_initial_data()

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("Оберіть вашу роль:")
        print("1. Адміністратор (Створення питань)")
        print("2. Студент (Проходження тесту)")
        print("0. Вихід з програми")

        role_choice = input("Ваш вибір > ")

        match role_choice:
            case "0":
                print("\n[Система]: Робота завершена. До побачення!")
                break

            case "1":
                login = input("Введіть логін адміна: ")
                user = Admin(login)

                user.show_menu(question_database)

            case "2":
                name = input("Введіть ваше ім'я: ")
                user = Student(name)

                user.show_menu(question_database)

            case _:
                print("Невірний вибір. Спробуйте ще раз.")

    print("\n[Система]: Очищення ресурсів...")
    del question_database

if __name__ == "__main__":
    main()