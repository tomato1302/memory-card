
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QRadioButton, QLabel, QGroupBox,
                             QHBoxLayout, QVBoxLayout, QButtonGroup)
from random import shuffle,randint

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card 3000")

lb_question = QLabel("Запитання")
btn_ok = QPushButton("Відповідь")

radioGroupBox = QGroupBox("Варіанти відповідей")

rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

radioGroup = QButtonGroup()
radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbtn_2)
radioGroup.addButton(rbtn_3)
radioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox("Результат")
lb_result = QLabel("Може правильно")
lb_correct = QLabel("Правильна відповідь")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, stretch=2, alignment=Qt.AlignHCenter)
ansGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=Qt.AlignCenter)
layout_line2.addWidget(radioGroupBox)
layout_line2.addWidget(ansGroupBox)
ansGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)

window.setLayout(layout_card)

def show_result():
    radioGroupBox.hide()
    ansGroupBox.show()
    btn_ok.setText("Наступне запитання")

def show_question():
    ansGroupBox.hide()
    radioGroupBox.show()
    btn_ok.setText("Відповідь")
    radioGroup.setExclusive(False)
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False)
    radioGroup.setExclusive(True)



    
    
# ! ТУТ ПОЧИНАЄМО ПИСАТИ
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res) 

    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Не правильно!")

def next_question():
    cur_question = randint(0, len(questions) - 1)
    q = questions[cur_question]
    ask(q)



def click_ok():
    if btn_ok.text() == "Відповідь":
        check_answer()
    else:
        next_question()


btn_ok.clicked.connect(click_ok)

questions = []
q1 = Question("Скільки буде квадратний корінь з 81?", "9", "10", "7", "8")

questions.append(q1)

next_question()
window.resize(600, 400)
window.show()
app.exec_()