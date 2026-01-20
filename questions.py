class AnswerKey:
    def __init__(self, correct_answer):
        self.value = correct_answer
        print(f"  [Деталь]: Ключ типу '{type(self.value).__name__}' створено.")

    def __del__(self):
        print(f"  [Деталь]: Ключ відповіді знищено.")

class Question:
    def __init__(self, text, correct_answer, difficulty=1):
        self.text = text
        self.difficulty = difficulty
        self.user_score = 0

        self.answer_key = AnswerKey(correct_answer)

        print(f"[Тест]: Питання '{self.text[:15]}...' (Базове) створено.")

    def check_answer(self, user_response):
        raise NotImplementedError("check_answer має бути реалізований у підкласах")

    def get_text(self):
        return f"{self.text} (Бали: {10 * self.difficulty})"

    def __del__(self):
        print(f"[Тест]: Питання '{self.text[:15]}...' знищено.")


# ВВІД ВІДПОВІДІ
class TextQuestion(Question):
    def check_answer(self, user_response):
        is_correct = str(user_response).strip().lower() == str(self.answer_key.value).lower()
        if is_correct:
            self.user_score = 10 * self.difficulty
            return True
        return False


# ВИБІР ОДНОГО
class OneChoiceQuestion(Question):
    def __init__(self, text, options, correct_idx, difficulty=1):
        super().__init__(text, correct_idx, difficulty)
        self.options = options

    def get_text(self):
        base = super().get_text()
        variants = "\n".join([f"{i + 1}. {opt}" for i, opt in enumerate(self.options)])
        return f"{base}\nВаріанти:\n{variants}"

    def check_answer(self, user_response):
        try:
            choice = int(user_response)
            is_correct = (choice == self.answer_key.value)
            if is_correct:
                self.user_score = 10 * self.difficulty
                return True
        except ValueError:
            pass
        return False


# ВИБІР ДЕКІЛЬКОХ
class MultiChoiceQuestion(Question):
    def __init__(self, text, options, correct_indices, difficulty=1):
        super().__init__(text, correct_indices, difficulty)
        self.options = options

    def get_text(self):
        base = super().get_text()
        variants = "\n".join([f"{i + 1}. {opt}" for i, opt in enumerate(self.options)])
        return f"{base}\n(Введіть номери через кому, наприклад: 1,3)\nВаріанти:\n{variants}"

    def check_answer(self, user_response):
        try:
            user_set = set(int(x.strip()) for x in user_response.split(','))
            correct_set = set(self.answer_key.value)

            if user_set == correct_set:
                self.user_score = 10 * self.difficulty
                return True
        except ValueError:
            pass
        return False


# ПОСЛІДОВНІСТЬ
class OrderQuestion(Question):
    def __init__(self, text, items, correct_order, difficulty=1):
        super().__init__(text, correct_order, difficulty)
        self.items = items

    def get_text(self):
        base = super().get_text()
        items_str = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(self.items)])
        return f"{base}\n(Розставте номери у правильному порядку через пробіл)\nЕлементи:\n{items_str}"

    def check_answer(self, user_response):
        try:
            user_order = [int(x) for x in user_response.replace(',', ' ').split()]
            if user_order == self.answer_key.value:
                self.user_score = 10 * self.difficulty
                return True
        except ValueError:
            pass
        return False


# ВІДПОВІДНІСТЬ
class MatchingQuestion(Question):
    def __init__(self, text, left_col, right_col, correct_pairs, difficulty=1):
        super().__init__(text, correct_pairs, difficulty)
        self.left = left_col
        self.right = right_col

    def get_text(self):
        base = super().get_text()
        left_str = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(self.left)])
        right_str = "\n".join([f"{chr(65 + i)}. {item}" for i, item in enumerate(self.right)])
        return (f"{base}\n(Формат відповіді: 1-B, 2-A)\n"
                f"Стовпчик 1:\n{left_str}\n\nСтовпчик 2:\n{right_str}")

    def check_answer(self, user_response):
        try:
            user_pairs = {}
            pairs = user_response.replace(' ', '').split(',')  # ["1-B", "2-A"]
            for p in pairs:
                k, v = p.split('-')
                user_pairs[k] = v.upper()

            if user_pairs == self.answer_key.value:
                self.user_score = 10 * self.difficulty
                return True
        except Exception:
            pass
        return False

    # FACTORY METHOD
class QuestionFactory:
    @staticmethod
    def create_question(q_type, data):
        text = data.get('text')
        difficulty = int(data.get('difficulty', 1))

        match q_type:
            case 'text':
                correct_answer = data.get('correct_answer')
                return TextQuestion(text, correct_answer, difficulty)

            case 'one_choice':
                options = data.get('options')
                correct_idx = int(data.get('correct_idx'))
                return OneChoiceQuestion(text, options, correct_idx, difficulty)

            case 'multi_choice':
                options = data.get('options')
                correct_indices = data.get('correct_indices')
                return MultiChoiceQuestion(text, options, correct_indices, difficulty)

            case 'order':
                items = data.get('items')
                correct_order = data.get('correct_order')
                return OrderQuestion(text, items, correct_order, difficulty)

            case 'matching':
                left = data.get('left')
                right = data.get('right')
                pairs = data.get('pairs')
                return MatchingQuestion(text, left, right, pairs, difficulty)

            case _:
                raise ValueError(f"Невідомий тип питання: {q_type}")