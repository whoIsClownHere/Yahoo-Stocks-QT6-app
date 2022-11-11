import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from CalendarWindow import CalendarWindow
from StockWindow import StocksWindow
from BackEnd import stocks_returns
from WorkWithHistory import add_item_to_history
from HistoryWindow import HistoryWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.history_window = None
        self.calendar = None
        self.stock_window = None

        self.setWindowTitle("Акции")
        self.resize(700, 300)

        self.main_layout = QVBoxLayout(self)

        self.title = QLabel(self)
        self.title.setText("Акции")

        # layout для ввода данных
        self.buttons_layout = QVBoxLayout(self)

        # layout для поля ввода акции
        self.write_stocks_layout = QHBoxLayout(self)

        # заголовок названия акции
        self.write_stocks_title = QLabel(self)
        self.write_stocks_title.setText("Название акций:")

        # поле для ввода названия акции
        self.write_stock = QLineEdit(self)

        self.write_stocks_layout.addWidget(self.write_stocks_title)
        self.write_stocks_layout.addWidget(self.write_stock)

        # layout для поля ввода веса акций
        self.write_width_layout = QHBoxLayout(self)

        # заголовок веса акций
        self.write_width_title = QLabel(self)
        self.write_width_title.setText("Вес акций в портфели:")

        # поле для ввода веса акций
        self.write_width = QLineEdit(self)

        self.write_width_layout.addWidget(self.write_width_title)
        self.write_width_layout.addWidget(self.write_width)

        # разделитель данных
        self.separator_layout = QHBoxLayout(self)

        # заголовок разделитель входных данных
        self.separator_title = QLabel(self)
        self.separator_title.setText("Разделитель вводных данных:")

        # поле для ввода разделителя входных данных
        self.separator = QLineEdit(self)
        self.separator.setText(", ")

        self.separator_layout.addWidget(self.separator_title)
        self.separator_layout.addWidget(self.separator)

        # layout для полей календаря
        self.date_layout = QHBoxLayout(self)

        # заголовок покупки акции
        self.date_from_title = QLabel(self)
        self.date_from_title.setText("Дата покупки акций:")

        # определение когда купил акцию
        self.date_from_button = QPushButton(self)
        self.date_from_button.setText("00.00.00")
        self.date_from_button.clicked.connect(self.show_calendar_for_date_from)

        # заголовок продажи акции
        self.date_to_title = QLabel(self)
        self.date_to_title.setText("Дата продажи:")

        # определение когда продал акцию
        self.date_to_button = QPushButton(self)
        self.date_to_button.setText("00.00.00")
        self.date_to_button.clicked.connect(self.show_calendar_for_date_to)

        self.date_layout.addWidget(self.date_from_title)
        self.date_layout.addWidget(self.date_from_button)
        self.date_layout.addWidget(self.date_to_title)
        self.date_layout.addWidget(self.date_to_button)

        # добавление в layout
        self.buttons_layout.addLayout(self.write_stocks_layout)
        self.buttons_layout.addLayout(self.write_width_layout)
        self.buttons_layout.addLayout(self.separator_layout)
        self.buttons_layout.addLayout(self.date_layout)

        self.result_button = QPushButton(self)
        self.result_button.setText("Получить данные")
        self.result_button.clicked.connect(self.show_stock_window)

        self.show_history = QPushButton(self)
        self.show_history.setText("Показать историю")
        self.show_history.clicked.connect(self.show_history_window)

        self.main_layout.addWidget(self.title)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addWidget(self.result_button)
        self.main_layout.addWidget(self.show_history)
        self.setLayout(self.main_layout)

    def show_calendar_for_date_from(self):
        self.calendar = CalendarWindow()
        if self.calendar.exec():
            year, month, day = self.calendar.calendar.selectedDate().getDate()
            self.date_from_button.setText(f"{year}-{month}-{day}")

    def show_calendar_for_date_to(self):
        self.calendar = CalendarWindow()
        if self.calendar.exec():
            year, month, day = self.calendar.calendar.selectedDate().getDate()
            self.date_to_button.setText(f"{year}-{month}-{day}")

    def show_stock_window(self):
        names, widths, date_from, date_to = self.get_name_and_dates()
        try:
            all_stocks = names.split(self.separator.text())
            width = list(map(float, widths.split(self.separator.text())))
            # add_item_to_history(names, widths, self.separator.text(), date_from, date_to)
        except ValueError:
            return "fsfs"
        stocks_returns(all_stocks, width, date_from, date_to)
        self.stock_window = StocksWindow(names, date_from, date_to)
        self.stock_window.show()

    def show_history_window(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def get_name_and_dates(self):
        return self.write_stock.text(), self.write_width.text(),\
               self.date_from_button.text(), self.date_to_button.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
