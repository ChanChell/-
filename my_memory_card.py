from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('мемори кард')
main_win.resize(600, 400)

class Qwest():
    def __init__(self, qwest, right_answer, wrong1, wrong2, wrong3):
        self.qwest = qwest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
question = QLabel('В каком году канал получил «золотую кнопку» от YouTube?')

RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
layoutH1 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutV2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutV2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutV3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutV3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutH1.addLayout(layoutV2)
layoutH1.addLayout(layoutV3)

RadioGroupBox.setLayout(layoutH1)

GroupBox2 = QGroupBox('Результат теста')
lk1 = QLabel('Правильно/Неправильно')
lk2 = QLabel('/')
layoutV6 = QVBoxLayout()
layoutV6.addWidget(lk1, alignment = Qt.AlignLeft)
layoutV6.addWidget(lk2, alignment = Qt.AlignCenter)

GroupBox2.setLayout(layoutV6)

answer_bt = QPushButton('Ответить')

layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()

layoutH4.addWidget(question, alignment = Qt.AlignCenter)
layoutH5.addWidget(answer_bt,  stretch = 2)
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutH4)
layout_main.addWidget(RadioGroupBox)

layout_main.addWidget(GroupBox2)
GroupBox2.hide()
layout_main.addLayout(layoutH5)
main_win.setLayout(layout_main)

def show_result():
    RadioGroupBox.hide()
    GroupBox2.show()
    answer_bt.setText('Следующий вопрос')

def show_question():
    GroupBox2.hide()
    RadioGroupBox.show()
    answer_bt.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Qwest):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.qwest)
    lk2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Правильных ответов:', main_win.score)
        print('рейтинг:', (main_win.score/main_win.total)*100)
    else: 
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('рейтинг:', (main_win.score/main_win.total)*100)
def show_correct(res):
    lk1.setText(res)
    show_result()
question_list = []
q1 = Qwest('Государственный язык бразили:', 'Португальский', 'Русский', 'Немецкий', 'Китайский')
q2 = Qwest('Автомат калашникова был изобреьён в: ', 'СССР', 'Германии', 'Великобритании', 'США')
q3 = Qwest('Как называется наивысшее соревновательное звание CSGO?', 'Всемирная Элита', 'Золотая Звезда', 'Великий Магистр', 'Легендарный Беркут')
q4 = Qwest('Сколько патронов в одном магазине АК-47?', '30', '47', '25', '32')
q5 = Qwest('Какой предмет не может иметь StatTrak?', 'Zeus x27', 'Shadow Daggers', 'Music Kit', 'M249')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)


def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    print('Всего вопросов:', main_win.total)

def start_test():
    if answer_bt.text() == 'Ответить':
        check_answer()
    else:
        next_question()



answer_bt.clicked.connect(start_test)
main_win.score = 0
main_win.total = 0
next_question()


main_win.show()
app.exec_()