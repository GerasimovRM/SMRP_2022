import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
from ui_file_browser import Ui_MainWindow
from PyQt5.uic import loadUi


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_name = None
        self.pushButton_load.clicked.connect(self.load_action)
        self.pushButton_save.clicked.connect(self.save_action)

    def load_action(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if not file_name:
            return

        self.file_name = file_name
        self.label_file_name.setText(file_name)
        with open(file_name, "r", encoding="utf-8") as input_file:
            data = input_file.read()
            self.textEdit.setText(data)

    def save_action(self):
        if not self.file_name:
            return
        with open(self.file_name, "w") as output_file:
            data = self.textEdit.toPlainText()
            output_file.write(data)


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
