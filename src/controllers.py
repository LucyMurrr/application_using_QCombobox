from PyQt5.QtSql import QSqlQuery

class AppController:
    def __init__(self, model, db_connector):
        self.model = model
        self.db_connector = db_connector

    def get_authors(self):
        query = QSqlQuery()
        query.exec_("SELECT id_teacher, fio FROM teachers")
        authors = {}
        while query.next():
            authors[query.value("fio")] = query.value("id_teacher")
        return authors

    def add_record(self, tname, tcontent, author_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO tests (tname, tcontent, teacher_id) VALUES (?, ?, ?)")
        query.addBindValue(tname)
        query.addBindValue(tcontent)
        query.addBindValue(author_id)
        if not query.exec_():
            print(f"Ошибка добавления записи: {query.lastError().text()}")

    def delete_record(self, row):
        self.model.removeRow(row)
        self.model.submitAll()