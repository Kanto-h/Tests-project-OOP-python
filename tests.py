# КЛАС-ЧАСТИНА (КОМПОЗИЦІЯ)
class TestStatistics:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0
        self.score_log = []  # Хронологія відповідей у пам'яті
        print("  [Статистика]: Бланк результатів створено.")

    def record_answer(self, is_correct, question_text, score):
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1

        status = "Вірно" if is_correct else "Невірно"
        self.score_log.append(f"{status} | {question_text[:30]}... (+{score if is_correct else 0} балів)")

    def show_detailed_report(self):
        print("\n" + "=" * 30)
        print("ЗВІТ ПО ПОТОЧНІЙ СЕСІЇ:")
        for entry in self.score_log:
            print(entry)
        print("=" * 30)

    def get_summary(self):
        percentage = (self.correct_answers / self.total_questions * 100) if self.total_questions > 0 else 0
        return f"Підсумок: {self.correct_answers} з {self.total_questions} ({percentage:.1f}%)"

    def __del__(self):
        print("  [Статистика]: Бланк результатів видалено.")

# КЛАС-ЦІЛЕ
class TestManager:
    def __init__(self, student_name):
        self.student_name = student_name
        self.question_list = []
        self.stats = TestStatistics()
        print(f"[Менеджер]: Сесія для {self.student_name} відкрита.")

    def add_question(self, question_object):
        self.question_list.append(question_object)

    def run_test(self):
        print(f"\n>>> ТЕСТУВАННЯ: {self.student_name} <<<")

        if not self.question_list:
            print("Помилка: Питання відсутні.")
            return

        for q in self.question_list:
            print(f"\n{q.get_text()}")

            answer = input("Відповідь: ")

            is_correct = q.check_answer(answer)

            self.stats.record_answer(is_correct, q.text, q.user_score)

            if is_correct:
                print("Правильно!")
            else:
                print("Неправильно.")

        print(f"\nТест завершено.")
        print(self.stats.get_summary())

        self.stats.show_detailed_report()

    def __del__(self):
        print(f"[Менеджер]: Сесія користувача {self.student_name} зачинена.")