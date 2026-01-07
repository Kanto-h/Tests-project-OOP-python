from questions import Question
from tests import TestManager

# 1. Создаем менеджера (Логика управления)
manager = TestManager("Иван Иванов")

# 2. Создаем пару объектов-вопросов (Базовые объекты)
q1 = Question("Столица Украины?", "Киев", difficulty=1)
q2 = Question("2 + 2 * 2 = ?", "6", difficulty=2)

# 3. Добавляем их в менеджер
manager.add_question(q1)
manager.add_question(q2)

# 4. Запускаем процесс
manager.run_test()

# 5. В конце лабы явно удаляем объекты, чтобы сработали деструкторы
del q1
del q2
del manager