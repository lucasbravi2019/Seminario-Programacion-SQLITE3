import sqlite3

pelicula = """CREATE TABLE pelicula (
            id integer primary key autoincrement,
            titulo text not null,
            año integer not null,
            duracion real not null, 
            nombre_estudio text not null
            )"""

estrella = """CREATE TABLE estrella (
            id integer primary key autoincrement,
            nombre text not null,
            direccion text not null,
            sexo text not null,
            fecha_nacimiento text not null
            )"""

estudio = """CREATE TABLE estudio (
            id integer primary key autoincrement,
            nombre text not null,
            direccion not null
            )"""

protagoniza = """CREATE TABLE protagoniza (
            id integer primary key autoincrement,
            titulo_pelicula text not null,
            año_pelicula text not null,
            nombre_estrella
            )"""


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('integrador')

    def migrate(self):
        print('Migrando')
        try:
            self.conn.execute(pelicula)
            self.conn.execute(estrella)
            self.conn.execute(estudio)
            self.conn.execute(protagoniza)
        except sqlite3.OperationalError:
            print('Table exists')
            self.conn.close()

    def select(self, query):
        with self.conn:
            cursor = self.conn.execute(query)
            return cursor.fetchall()

    def execute(self, query, params):
        with self.conn:
            self.conn.execute(query, params)
            self.conn.commit()
