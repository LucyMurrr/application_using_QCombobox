Приложение для рабочего стола, взаимодействующее с postgreSQL БД.
Позволяет создавать задачи, имеет редактируемые текстовые поля. Значения полей колонки "Автор" изменяются посредством выпадающего списка. 

**1. git clone

**2. Создать БД tasks:

**  sudo -u <user> psql

**  CREATE DATABASE tasks;

**3. Создать таблицы. См. sql_scripts -> create_table.sql

**  Заполнить таблицы базовыми значениями. См. sql_scripts -> insert_table.sql

**4. Изменить параметры подключения в config.py

**5. cd application_using_QCombobox/src
**   python3 main.py



