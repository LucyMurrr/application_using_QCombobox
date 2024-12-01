from PyQt5.QtWidgets import QDialog, QLineEdit, QTextEdit, QComboBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class AddRecordDialog(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить запись")
        self.name_input = QLineEdit(self)
        self.content_input = QTextEdit(self)
        self.author_input = QComboBox(self)
        authors = controller.get_authors()
        for fio, teacher_id in authors.items():
            self.author_input.addItem(fio, teacher_id)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Название"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Содержание"))
        layout.addWidget(self.content_input)
        layout.addWidget(QLabel("Автор"))
        layout.addWidget(self.author_input)
        button_layout = QHBoxLayout()
        add_button = QPushButton("Добавить", self)
        cancel_button = QPushButton("Отмена", self)
        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        add_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

    def get_data(self):
        return {
            "tname": self.name_input.text().strip(),
            "tcontent": self.content_input.toPlainText().strip(),
            "author_id": self.author_input.currentData()
        }