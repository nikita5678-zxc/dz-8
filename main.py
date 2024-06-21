import json
import random

"""Списки для вывода статистики"""
questions_ = []
points = []

"""Абстракция Question и методы"""
class Question():

    def __init__(self, text_question, difficulty, correct_answer, answer=None, points=0, asked=False):
        self.text_question = text_question
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.asked = asked
        self.answer = answer
        self.points = points

    def get_points(self):
        if self.difficulty == "1":
            self.points = 10
        elif self.difficulty == "2":
            self.points = 20
        elif self.difficulty == "3":
            self.points = 30
        elif self.difficulty == "4":
            self.points = 40
        elif self.difficulty == "5":
            self.points = 50
        return self.points

    def is_correct(self):
        if self.answer == self.correct_answer:
            return True
        else:
            return False

    def build_question(self):
        return f"Вопрос: {self.text_question} \nСложность {self.difficulty}/5"

    def build_feedback(self):
        if self.answer == self.correct_answer:
            questions_.append(True)
            points.append(self.points)
            return f"Ответ верный, получено {self.points} баллов"
        else:
            questions_.append(False)
            return f"Ответ неверный, верный ответ - {self.correct_answer}"


class End():
    def print_data_of_programm(self):
        return f"Вот и всё! \nОтвечено на {questions_.count(True)} из {len(questions_)} \nНабрано {sum(points)} баллов"

print("Игра начинается!")


"""Часть программы, которя будет задавать случайные вопросы"""
random_question = []
with open("questions.txt") as file:
    file = json.load(file)
    for question in file:
        random_question.append(question)

for question in random_question[:]:
    que = random.sample(random_question, 1)[0]
    print(f"Вопрос: {que["q"]} \nСложность {que["d"]}/5")
    random_question.remove(que)
    answer = input().lstrip()
    data_question = Question(f"{que["q"]}", f"{que["d"]}", f"{que["a"]}", f"{answer}")
    data_question.get_points()
    print(data_question.build_feedback())
    print("---------")

"""Вывод результатов"""
end_ = End()
print(end_.print_data_of_programm())