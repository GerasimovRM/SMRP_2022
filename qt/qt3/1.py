import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QTableWidgetItem
from ui_list import Ui_MainWindow
import requests



# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_users)
        self.tableWidget.doubleClicked.connect(self.get_todos)
        self.get_users()

    def get_users(self):
        self.tableWidget.setRowCount(0)
        response = requests.get("https://jsonplaceholder.typicode.com/users").json()
        for user in response:
            current_row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(current_row)
            self.tableWidget.setItem(current_row, 0, QTableWidgetItem(str(user["id"])))
            self.tableWidget.setItem(current_row, 1, QTableWidgetItem(str(user["name"])))
            self.tableWidget.setItem(current_row, 2, QTableWidgetItem(str(user["email"])))

    def get_todos(self, index):
        row = index.row()
        user_id = int(self.tableWidget.item(row, 0).text())
        response = requests.get("https://jsonplaceholder.typicode.com/todos").json()
        todos = list(filter(lambda todo: todo["userId"] == user_id, response))
        self.comboBox.clear()
        for todo in todos:
            print(todo)
            base_str = f"{todo['id']} {todo['title']}"
            if todo["completed"]:
                base_str += " ✅"
            else:
                base_str += " ❌"
            self.comboBox.addItem(base_str)


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