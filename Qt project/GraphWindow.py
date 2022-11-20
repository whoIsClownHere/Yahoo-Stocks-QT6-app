from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from BuildGraphs import build_pie, build_boxplot, build_portfolio_chart


class GraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Какой график построить")
        self.resize(500, 300)

        # основной layout
        self.main_layout = QVBoxLayout(self)

        self.title = QLabel(self)
        self.title.setText("Графики")

        # построить основной график
        self.portfolio_chart = QPushButton(self)
        self.portfolio_chart.setText("Построить общий график портфеля")
        self.portfolio_chart.clicked.connect(self.build_portfolio_chart)

        # построить график "пирог"
        self.pie_button = QPushButton(self)
        self.pie_button.setText("Построить соотношение количества приростов и потерь портфеля")
        self.pie_button.clicked.connect(build_pie)

        # построить график "ящик с усами"
        self.boxplot_button = QPushButton(self)
        self.boxplot_button.setText("Построить ящик с усами для портфеля")
        self.boxplot_button.clicked.connect(build_boxplot)

        # добовление элементов в layout
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.portfolio_chart)
        self.main_layout.addWidget(self.pie_button)
        self.main_layout.addWidget(self.boxplot_button)

        self.setLayout(self.main_layout)

    @staticmethod
    def build_pie():
        build_pie()

    @staticmethod
    def build_boxplot():
        build_boxplot()

    @staticmethod
    def build_portfolio_chart():
        build_portfolio_chart()
