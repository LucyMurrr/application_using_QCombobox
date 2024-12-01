from PyQt5.QtSql import QSqlDatabase

def create_connection():
    db = QSqlDatabase.addDatabase("QPSQL")
    db.setHostName("localhost")
    db.setPort(5432)
    db.setDatabaseName("tasks")
    db.setUserName("postgres")
    db.setPassword("1234")

    if not db.open():
        print(f"Ошибка подключения к базе данных: {db.lastError().text()}")
        return False
    print("Подключение к базе данных успешно.")
    return True
