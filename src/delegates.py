from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt5.QtCore import Qt

class TeacherComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, authors, parent=None):
        super().__init__(parent)
        self.authors = authors

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        for author_fio, author_id in self.authors.items():
            editor.addItem(author_fio, author_id)
        return editor

    def setEditorData(self, editor, index):
        teacher_id = index.model().data(index, Qt.DisplayRole)
        for i in range(editor.count()):
            if editor.itemData(i) == teacher_id:
                editor.setCurrentIndex(i)
                break

    def setModelData(self, editor, model, index):
        teacher_id = editor.itemData(editor.currentIndex())
        model.setData(index, teacher_id)