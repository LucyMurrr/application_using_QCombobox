from PyQt5.QtSql import QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtCore import Qt

class TestModel(QSqlRelationalTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTable("tests")
        self.setRelation(3, QSqlRelation("teachers", "id_teacher", "fio"))
        self.select()

        self.setHeaderData(0, Qt.Horizontal, "ID")
        self.setHeaderData(1, Qt.Horizontal, "Название задачи")
        self.setHeaderData(2, Qt.Horizontal, "Содержание")
        self.setHeaderData(3, Qt.Horizontal, "Автор")

        def data(self, index, role=Qt.DisplayRole):
            if role == Qt.DisplayRole and index.column() == 3:
                return super().data(index, role)
            return super().data(index, role)