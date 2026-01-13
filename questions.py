class AnswerKey:
    def __init__(self, correct_answer):
        self.value = correct_answer
        print(f"  [Деталь]: Ключ відповіді '{self.value}' створено.")

    def verify(self, user_response):
        return str(user_response).strip().lower() == str(self.value).lower()

    def __del__(self):
        print(f"  [Деталь]: Ключ відповіді '{self.value}' знищено разом з питанням.")


class Question:
    def __init__(self, text, correct_answer, difficulty=1):
        self.text = text
        self.difficulty = difficulty
        self.user_score = 0

        self.answer_key = AnswerKey(correct_answer)

        print(f"[Тест]: Об'єкт питання '{self.text[:20]}...' створений.")

    def check_answer(self, response):
        if self.answer_key.verify(response):
            self.user_score = 10 * self.difficulty
            return True
        return False

    def __del__(self):
        print(f"[Тест]: Об'єкт питання '{self.text[:20]}...' знищений.")