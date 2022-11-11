from PyQt6.QtWidgets import QDialog, QCalendarWidget, QVBoxLayout, QPushButton


class CalendarWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выберите дату")
        self.resize(500, 400)

        self.main_layout = QVBoxLayout(self)
        self.calendar = QCalendarWidget(self)

        self.end_button = QPushButton(self)
        self.end_button.setText("Сохранить")
        self.end_button.clicked.connect(self.accept)

        self.main_layout.addWidget(self.calendar)
        self.main_layout.addWidget(self.end_button)

        self.setLayout(self.main_layout)
