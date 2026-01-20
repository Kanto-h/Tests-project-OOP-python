class ITestStrategy:

    def process_question(self, question, stats):
        raise NotImplementedError("Метод process_question має бути реалізований")


class TrainingStrategy(ITestStrategy):
    def process_question(self, question, stats):
        print(f"\n[Тренування] {question.get_text()}")
        answer = input("Ваша відповідь: ")

        is_correct = question.check_answer(answer)
        stats.record_answer(is_correct, question.text, question.user_score)

        if is_correct:
            print("Правильно! Молодець.")
        else:
            print(f"Неправильно. Правильна відповідь була: {question.answer_key.value}")


class ExamStrategy(ITestStrategy):
    def process_question(self, question, stats):
        print(f"\n[Екзамен] {question.get_text()}")
        answer = input("Відповідь: ")

        is_correct = question.check_answer(answer)
        stats.record_answer(is_correct, question.text, question.user_score)

        print("Відповідь прийнята.")


class TestStatistics:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0
        self.score_log = []
        print("  [Статистика]: Бланк створено.")

    def record_answer(self, is_correct, question_text, score):
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1

        status = "Вірно" if is_correct else "Невірно"
        self.score_log.append(f"{status} | {question_text[:30]}... (+{score if is_correct else 0} балів)")

    def show_detailed_report(self):
        print("\n" + "=" * 30)
        print("ЗВІТ ПО СЕСІЇ:")
        for entry in self.score_log:
            print(entry)
        print("=" * 30)

    def get_summary(self):
        percentage = (self.correct_answers / self.total_questions * 100) if self.total_questions > 0 else 0
        return f"Підсумок: {self.correct_answers} з {self.total_questions} ({percentage:.1f}%)"

    def __del__(self):
        print("  [Статистика]: Бланк видалено.")

class TestManager:
    def __init__(self, student_name, strategy=None):
        self.student_name = student_name
        self.question_list = []
        self.stats = TestStatistics()

        if strategy is None:
            self.strategy = TrainingStrategy()
        else:
            self.strategy = strategy

        print(f"[Менеджер]: Сесія для {self.student_name} відкрита. Режим: {type(self.strategy).__name__}")

    def add_question(self, question_object):
        self.question_list.append(question_object)

    def run_test(self):
        print(f"\n>>> ТЕСТУВАННЯ: {self.student_name} <<<")

        if not self.question_list:
            print("Помилка: Питання відсутні.")
            return

        for q in self.question_list:
            self.strategy.process_question(q, self.stats)

        print(f"\nТест завершено.")
        print(self.stats.get_summary())
        self.stats.show_detailed_report()

    def __del__(self):
        print(f"[Менеджер]: Сесія користувача {self.student_name} зачинена.")