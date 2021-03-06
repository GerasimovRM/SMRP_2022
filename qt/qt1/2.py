import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from ui_calc_two_number import Ui_MainWindow
from PyQt5.uic import loadUi


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # Зададим размер и положение нашего виджета,
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sum_two_numbers)
        self.pushButton_2.clicked.connect(self.sum_two_numbers)

    def sum_two_numbers(self):
        send = self.sender()
        print(send.text())
        res1 = self.lineEdit_1.text()
        if res1:
            number1 = float(res1)
        res2 = self.lineEdit_2.text()
        if res2:
            number2 = float(res2)
        if res1 and res2:
            self.label_result.setText(str(number1 + number2))



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())