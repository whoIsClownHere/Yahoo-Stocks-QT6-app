from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from StockWindow import StocksWindow
from BackEnd import stocks_returns
from WorkWithHistory import get_history, clear_history


class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stock_window = None
        self.setWindowTitle("История")
        self.resize(300, 300)
        self.main_layout = QVBoxLayout(self)

        # for name, weight, divider, date_from, date_to in get_history():
        #     self.stock_layout = QHBoxLayout(self)
        #
        #     self.title = QLabel(self)
        #     self.title.setText(f"{name}, {weight}, {divider}, {date_from}, {date_to}")
        #
        #     self.button = QPushButton(self)
        #     self.button.setText("Повторить")
        #
        #     self.stock_layout.addWidget(self.title)
        #     self.stock_layout.addWidget(self.button)
        #
        #     self.main_layout.addLayout(self.stock_layout)

        self.clear_button = QPushButton(self)
        self.clear_button.setText("Очистить историю")
        self.clear_button.clicked.connect(self.clear_history)

        self.main_layout.addWidget(self.clear_button)

        self.setLayout(self.main_layout)

    def show_stock_window(self):
        names, widths, date_from, date_to, separator = self.get_name_and_dates()
        all_stocks = names.split(self.separator)
        width = list(map(float, widths.split(self.separator)))
        stocks_returns(all_stocks, width, date_from, date_to)
        self.stock_window = StocksWindow(names, date_from, date_to)
        self.stock_window.show()

    def get_name_and_dates(self):
        return self.write_stock, self.write_width,\
               self.date_from_button, self.date_to_button, self.separator

    @staticmethod
    def clear_history():
        clear_history()
