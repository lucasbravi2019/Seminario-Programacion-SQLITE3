from entity.estrella import Estrella


class EstrellaReposository:

    def __init__(self, conn):
        self.conn = conn

    def crear_estrella(self, params):
        query = 'insert into estrella (nombre, direccion, sexo, fecha_nacimiento) values (?, ?, ?, ?)'
        self.conn.execute(query, params)

    def editar_estrella(self, params):
        query = 'update estrella set nombre = ?, direccion = ?, sexo = ?, fecha_nacimiento = ? where id = ?'
        self.conn.execute(query, params)

    def borrar_estrella(self, id):
        query = 'delete from estrella where id = ?'
        self.conn.execute(query, params=[id])

    def ver_estrellas(self):
        rows = self.conn.select('select id, nombre, direccion, sexo, fecha_nacimiento from estrella')
        estrellas = []
        for fila in rows:
            estrella = Estrella(fila[1], fila[2], fila[3], fila[4], fila[0])
            estrellas.append(estrella)

        return estrellas

    def ver_nombres_estrellas(self):
        rows = self.conn.select('select id, nombre from estrella')
        estrellas = []
        for fila in rows:
            estrella = (fila[0], fila[1])
            estrellas.append(estrella)

        return estrellas
