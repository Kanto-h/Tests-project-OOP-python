from admin import Admin, Student
from questions import QuestionFactory

def create_initial_data():

    demo_list = []

    data_q1 = {
        "text": "Столиця Франції?",
        "correct_answer": "Париж",
        "difficulty": 1
    }
    q1 = QuestionFactory.create_question("text", data_q1)

    data_q2 = {
        "text": "Скільки біт у байті?",
        "options": ["4", "8", "16"],
        "correct_idx": 2,
        "difficulty": 1
    }
    q2 = QuestionFactory.create_question("one_choice", data_q2)

    data_q3 = {
        "text": "Що з цього фрукти?",
        "options": ["Яблуко", "Картопля", "Груша"],
        "correct_indices": [1, 3],
        "difficulty": 2
    }
    q3 = QuestionFactory.create_question("multi_choice", data_q3)

    demo_list.extend([q1, q2, q3])
    return demo_list

def main():
    print("\n" + "=" * 50)
    print("      СИСТЕМА ТЕСТУВАННЯ (ЛР №4)      ")
    print("      Патерни: Factory Method & Strategy      ")
    print("=" * 50)

    question_database = create_initial_data()

    while True:
        print("\n    ГОЛОВНЕ МЕНЮ    ")
        print("Оберіть вашу роль:")
        print("1. Адміністратор")
        print("2. Студент")
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