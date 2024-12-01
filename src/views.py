from PyQt5.QtWidgets import (
    QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget, QGridLayout, QHeaderView
)
from PyQt5.QtCore import Qt
from models import TestModel
from controllers import AppController
from ui_dialog import AddRecordDialog
from db_connector import DatabaseConnector
from delegates import TeacherComboBoxDelegate

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задачи")
        self.resize(800, 600)
        central_widget = QWidget(self)
        layout = QGridLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.db_connector = DatabaseConnector()
        self.model = TestModel(self)
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.controller = AppController(self.model, self.db_connector)
        self.setup_table()
        self.add_button = QPushButton("Добавить")
        self.delete_button = QPushButton("Удалить")
        layout.addWidget(self.table_view, 0, 0, 1, 2)
        layout.addWidget(self.add_button, 1, 0)
        layout.addWidget(self.delete_button, 1, 1)
        self.add_button.clicked.connect(self.add_record)
        self.delete_button.clicked.connect(self.delete_record)

    def setup_table(self):
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        authors = self.controller.get_authors()
        delegate = TeacherComboBoxDelegate(authors)
        self.table_view.setItemDelegateForColumn(3, delegate)

    def add_record(self):
        dialog = AddRecordDialog(self.controller)
        if dialog.exec_():
            data = dialog.get_data()
            self.controller.add_record(data["tname"], data["tcontent"], data["author_id"])
            self.model.select()

    def delete_record(self):
        selected_index = self.table_view.currentIndex()
        if selected_index.isValid():
            self.controller.delete_record(selected_index.row())
            self.model.select()