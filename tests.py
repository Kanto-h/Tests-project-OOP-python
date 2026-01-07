class TestManager:
    def __init__(self, student_name):
        self.student_name = student_name
        self.question_list = []
        self.total_score = 0
        print(f"[Менеджер]: Сесія для {self.student_name} відкрита.")

    def add_question(self, question_object):
        self.question_list.append(question_object)

    def run_test(self):
        print(f"\n Починаємо тест для: {self.student_name} ")
        for q in self.question_list:
            print(f"\nПитання: {q.text}")
            answer = input("Відповідь: ")
            if q.check_answer(answer):
                print("Правильно")
                self.total_score += q.user_score
            else:
                print(f"Не правильно. Правильна відповідь: {q.correct_answer}")

        print(f"\nТест завершено. Сумарний бал: {self.total_score}")

    def __del__(self):
        print(f"[Менеджер]: Сесія користувача {self.student_name} зачинена и очищена.")