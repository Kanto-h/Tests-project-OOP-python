from questions import Question
from tests import TestManager

print("      ПОЧАТОК ПРОГРАМИ      \n")

manager = TestManager("убубэ")

q1 = Question("Столиця Франції?", "Париж", difficulty=1)
q2 = Question("Скільки біт у байті?", "8", difficulty=2)

manager.add_question(q1)
manager.add_question(q2)

manager.run_test()

print("\n      ДЕМОНСТРАЦІЯ ЗНИЩЕННЯ ОБ'ЄКТІВ (ЛР №2)      ")

print("\n> Видаляємо Менеджера")
del manager

print("\n> Видаляємо Питання")
del q1
del q2

print("\n      КІНЕЦЬ ПРОГРАМИ      ")