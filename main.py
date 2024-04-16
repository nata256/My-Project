from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
app = QApplication([])

window = QWidget()
window.resize(200, 310)

window.setWindowTitle("Menu")
window.setStyleSheet("background-image: url('kotik fon.jpg')")
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
window1.setStyleSheet("background-color: 'red'")
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

def show_joke():
    with open("anekdot.txt", "r", encoding="UTF-8") as file:
        date = file.readlines()
        Jokes.setText(choice(date))
        # print(date.count("\n"))
        

def read():
    window1.show()
    window.hide()

butn1.clicked.connect(read)
button2.clicked.connect(show_joke)

app.exec()

