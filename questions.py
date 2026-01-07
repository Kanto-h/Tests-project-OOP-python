class Question:
    def __init__(self, text, correct_answer, difficulty=1):
        self.text = text
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.user_score = 0
        print(f"[Тест]: Об'єкт питання '{self.text[:20]}...' створений.")

    def check_answer(self, response):
        if str(response).strip().lower() == str(self.correct_answer).lower():
            self.user_score = 10 * self.difficulty
            return True
        return False

    def __del__(self):
        print(f"[Тест]: Об'єкт питання '{self.text[:20]}...' знищений.")