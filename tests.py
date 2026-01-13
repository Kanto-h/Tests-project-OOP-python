class TestStatistics:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0
        print("  [Статистика]: Бланк результатів створено (Композиція).")

    def record_answer(self, is_correct):
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1

    def get_summary(self):
        percentage = (self.correct_answers / self.total_questions * 100) if self.total_questions > 0 else 0
        return f"Результат: {self.correct_answers} з {self.total_questions} правильних ({percentage}%)."

    def __del__(self):
        print("  [Статистика]: Бланк результатів знищено разом з менеджером.")

class TestManager:
    def __init__(self, student_name):
        self.student_name = student_name
        # АГРЕГАЦІЯ: список питань (самі питання існують незалежно від менеджера)
        self.question_list = []
        # КОМПОЗИЦІЯ: об'єкт статистики (не існує без менеджера)
        self.stats = TestStatistics()

        print(f"[Менеджер]: Сесія для {self.student_name} відкрита.")

    def add_question(self, question_object):
        self.question_list.append(question_object)

    def run_test(self):
        print(f"\n      Починаємо тест для: {self.student_name}         ")

        if not self.question_list:
            print("Список питань порожній!")
            return

        for q in self.question_list:
            print(f"\nПитання: {q.text}")
            answer = input("Відповідь: ")

            is_correct = q.check_answer(answer)
            self.stats.record_answer(is_correct)

            if is_correct:
                print("Правильно!")
            else:
                print("Не правильно.")

        print(f"\nТест завершено. {self.stats.get_summary()}")

    def __del__(self):
        print(f"[Менеджер]: Сесія користувача {self.student_name} зачинена.")