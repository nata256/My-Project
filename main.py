from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
app = QApplication([])

window = QWidget()
window.resize(200, 310)

window.setWindowTitle("Menu")
window.setStyleSheet(""".QWidget {background-image: url('kotik fon.png')})
                     QPushButton {backgrond-color: pink; color: black}""")
window.show()

butn1 = QPushButton("Прочитати")
butn2 = QPushButton("Додати")

main_line1 = QVBoxLayout()
main_line1.addWidget(butn1)
main_line1.addWidget(butn2)
window.setLayout(main_line1)

window1 = QWidget()
window1.resize(400, 250)

window1.setWindowTitle("Jokes")
window1.setStyleSheet("background-image: url('lapki fon.jpg')")
#window1.show()

button1 = QPushButton("Меню")
button2 = QPushButton("Анекдот")

main_line2 = QHBoxLayout()
line2 = QVBoxLayout()
line2.addWidget(button1)
line2.addWidget(button2)

Jokes = QLabel("гугу")
main_line2.addLayout(line2, stretch=1)
main_line2.addWidget(Jokes, stretch=2)
window1.setLayout(main_line2)

window2 = QWidget()
window2.resize(400, 250)

window2.setWindowTitle("Add")
window2.setStyleSheet("background-color: 'pink'")
#window2.show()

buttn1 = QPushButton("Меню")
buttn2 = QPushButton("Додати")
new_jokes = QLineEdit()

line3 = QVBoxLayout()
line3.addWidget(buttn1)
line3.addWidget(buttn2)
line3.addWidget(new_jokes)
window2.setLayout(line3)

def show_joke():
    with open("anekdot.txt", "r", encoding="UTF-8") as file:
        date = file.readlines()
        Jokes.setText(choice(date))
        # print(date.count("\n"))
        
def menu():
    window1.hide()
    window.show()

def read():
    window1.show()
    window.hide()

def add():
    window2.show()
    window.hide()

def meny():
    window2.hide()
    window.show()

butn1.clicked.connect(read)
button2.clicked.connect(show_joke)
button1.clicked.connect(menu)
butn2.clicked.connect(add)
buttn1.clicked.connect(meny)


app.exec()

