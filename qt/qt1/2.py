import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from ui_calc_two_number import Ui_MainWindow


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # Зададим размер и положение нашего виджета,
        self.setupUi(self)


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