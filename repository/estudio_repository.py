from entity.estudio import Estudio


class EstudioRepository:

    def __init__(self, conn):
        self.conn = conn

    def crear_estudio(self, params):
        query = 'insert into estudio (nombre, direccion) values (?, ?)'
        self.conn.execute(query, params)

    def editar_estudio(self, params):
        query = 'update estudio set nombre = ?, direccion = ? where id = ?'
        self.conn.execute(query, params)

    def borrar_estudio(self, id):
        query = 'delete from estudio where id = ?'
        self.conn.execute(query, params=[id])

    def ver_estudios(self):
        rows = self.conn.select('select id, nombre, direccion from estudio')
        estudios = []
        for fila in rows:
            estudio = Estudio(fila[1], fila[2], fila[0])
            estudios.append(estudio)

        return estudios

    def ver_nombres_estudios(self):
        rows = self.conn.select('select id, nombre from estudio')
        estudios = []
        for fila in rows:
            estudio = (fila[0], fila[1])
            estudios.append(estudio)

        return estudios
