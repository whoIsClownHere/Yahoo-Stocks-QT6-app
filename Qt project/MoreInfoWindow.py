import pandas as pd
from PyQt6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem


class MoreInfoWindow(QWidget):
    def __init__(self):
        super(MoreInfoWindow, self).__init__()
        self.resize(700, 500)

        self.main_layout = QVBoxLayout(self)

        self.stock_table = QTableWidget(self)
        self.load_data()

        self.main_layout.addWidget(self.stock_table)

        self.setLayout(self.main_layout)

    def load_data(self):
        stock_data = pd.read_csv('Data/more_info.csv')

        self.stock_table.setRowCount(stock_data.shape[0])
        self.stock_table.setColumnCount(stock_data.shape[1])

        for row in stock_data.iterrows():
            values = row[1]
            for col_ind, value in enumerate(values):
                table_item = QTableWidgetItem(str(value))
                self.stock_table.setItem(row[0], col_ind, table_item)

        self.stock_table.setColumnWidth(1, 300)
