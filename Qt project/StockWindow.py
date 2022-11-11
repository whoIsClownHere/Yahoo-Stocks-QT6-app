import pandas as pd
from PyQt6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QLineEdit, QPushButton
from MoreInfoWindow import MoreInfoWindow
from BackEnd import get_more_info
from GraphWindow import GraphWindow


class StocksWindow(QWidget):
    def __init__(self, name, date_from, date_to):
        super(StocksWindow, self).__init__()
        self.graphWindow = None
        self.more_info_window = None
        self.resize(700, 500)

        self.main_layout = QVBoxLayout(self)

        self.table_info = QLineEdit(self)
        self.table_info.setText(f"Акции {name} в период с {date_from} по {date_to}")
        self.table_info.setEnabled(False)

        self.stock_table = QTableWidget(self)
        self.load_data()

        self.graphics_button = QPushButton(self)
        self.graphics_button.setText("Построить график")
        self.graphics_button.clicked.connect(self.show_graph_window)

        self.more_info_button = QPushButton(self)
        self.more_info_button.setText("Показать важную информацию из таблицы")
        self.more_info_button.clicked.connect(self.show_more_info_window)

        self.main_layout.addWidget(self.table_info)
        self.main_layout.addWidget(self.stock_table)
        self.main_layout.addWidget(self.graphics_button)
        self.main_layout.addWidget(self.more_info_button)

        self.setLayout(self.main_layout)

    def load_data(self):
        stock_data = pd.read_csv('Data/stocks_returns.csv')

        self.stock_table.setRowCount(stock_data.shape[0])
        self.stock_table.setColumnCount(stock_data.shape[1])

        for row in stock_data.iterrows():
            values = row[1]
            for col_ind, value in enumerate(values):
                table_item = QTableWidgetItem(str(value))
                self.stock_table.setItem(row[0], col_ind, table_item)

        self.stock_table.setColumnWidth(1, 300)

    def show_more_info_window(self):
        get_more_info('Data/stocks_returns.csv')
        self.more_info_window = MoreInfoWindow()
        self.more_info_window.show()

    def show_graph_window(self):
        self.graphWindow = GraphWindow()
        self.graphWindow.show()
