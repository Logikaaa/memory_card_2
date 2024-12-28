from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSpinBox

win_width = 600
win_height = 500

window = QWidget()
window.resize(win_width, win_height)
window.setWindowTitle('Memory Card')
window.move(300, 300)

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
timer = QSpinBox()
timer.setValue(30)

timer_text = QLabel('секунд')

line_top = QHBoxLayout()
line_top.addWidget(btn_menu, alignment=(Qt.AlignLeft | Qt.AlignTop))
line_top.addWidget(btn_rest, alignment=(Qt.AlignRight | Qt.AlignTop))
line_top.addWidget(timer, alignment=(Qt.AlignRight | Qt.AlignTop))
line_top.addWidget(timer_text, alignment=(Qt.AlignRight | Qt.AlignTop))



RadioGroupBox = QGroupBox('Варіанти відповідей')

RadioGroup = QButtonGroup()

r1 = QRadioButton('1')
r2 = QRadioButton('2')
r3 = QRadioButton('3')
r4 = QRadioButton('4')

RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()

l2.addWidget(r1)
l2.addWidget(r2)
l3.addWidget(r3)
l3.addWidget(r4)

l1.addLayout(l2)
l1.addLayout(l3)

RadioGroupBox.setLayout(l1)

AnsGroupBox = QGroupBox('Результат')
ans_result = QLabel('')
ans_correct = QLabel('')

l_rez = QVBoxLayout()
l_rez.addWidget(ans_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
l_rez.addWidget(ans_correct, stretch=2)
AnsGroupBox.setLayout(l_rez)
AnsGroupBox.hide()

main_line = QVBoxLayout()

main_line.addLayout(line_top)

question = QLabel('Питання')

main_line.addWidget(question, alignment=(Qt.AlignCenter))
main_line.addWidget(RadioGroupBox)
main_line.addWidget(AnsGroupBox)

btn = QPushButton('Відповісти')
main_line.addWidget(btn, alignment=(Qt.AlignCenter))

window.setLayout(main_line)

def switch_screen():
    if btn.text() == 'Відповісти':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn.setText("Наступне питання")
    else:
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn.setText('Відповісти')

btn.clicked.connect(switch_screen)


window.show()


