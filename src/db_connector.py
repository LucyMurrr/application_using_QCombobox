from PyQt5.QtSql import QSqlQuery

class DatabaseConnector:
    def fetch_authors(self):
        query = QSqlQuery("SELECT id_teacher, fio FROM teachers;")
        authors = []
        while query.next():
            authors.append(query.value("fio"))
        return authors