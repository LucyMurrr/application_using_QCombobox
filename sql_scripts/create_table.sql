CREATE TABLE teachers (
    id_teacher SERIAL PRIMARY KEY,
    fio TEXT NOT NULL
);

CREATE TABLE tests (
    id SERIAL PRIMARY KEY,
    tname TEXT NOT NULL,
    tcontent TEXT NOT NULL,
    teacher_id INTEGER REFERENCES teachers (id_teacher)
);
