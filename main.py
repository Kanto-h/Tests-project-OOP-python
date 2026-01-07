from questions import Question
from tests import TestManager

manager = TestManager("Неуч")

# объект-вопрос
q1 = Question("Хто проживає в ананасі у морі на дні?", "Губка Боб", difficulty=1)
q2 = Question("?", "6", difficulty=2)

manager.add_question(q1)
manager.add_question(q2)

manager.run_test()

del q1
del q2
del manager