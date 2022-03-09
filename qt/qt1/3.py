import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from ui_calc import Ui_MainWindow


# Унаследуем наш класс от простейшего графического примитива QWidget
class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # Зададим размер и положение нашего виджета,
        self.setupUi(self)
        for button in self.findChildren(QPushButton):
            button.clicked.connect(self.common_slot)

    def common_slot(self):
        sender = self.sender()
        sender_text = sender.text()
        if sender_text in "01234565789()+-/*.":
            current_text = self.lineEdit.text()
            self.lineEdit.setText(current_text + sender_text)
        elif sender_text == "=":
            current_text = self.lineEdit.text()
            result = eval(current_text)
            self.lineEdit.setText(str(result))

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Calculator()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())