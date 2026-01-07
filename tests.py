class TestManager:
    def __init__(self, student_name):
        self.student_name = student_name
        self.question_list = []
        self.total_score = 0
        print(f"[Менеджер]: Сессия для {self.student_name} открыта.")

    def add_question(self, question_object):
        self.question_list.append(question_object)

    def run_test(self):
        print(f"\n--- Начинаем тест для: {self.student_name} ---")
        for q in self.question_list:
            print(f"\nВопрос: {q.text}")
            answer = input("Ваш ответ: ")
            if q.check_answer(answer):
                print("Верно!")
                self.total_score += q.user_score
            else:
                print(f"Неверно. Правильный ответ: {q.correct_answer}")

        print(f"\nТест завершен. Итоговый балл: {self.total_score}")

    def __del__(self):
        print(f"[Менеджер]: Сессия пользователя {self.student_name} закрыта и очищена.")