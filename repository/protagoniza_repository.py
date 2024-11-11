from entity.protagoniza import Protagoniza


class ProtagonizaRepository:

    def __init__(self, conn):
        self.conn = conn

    def crear_protagonista(self, params):
        query = 'insert into protagoniza (titulo_pelicula, año_pelicula, nombre_estrella) values (?, ?, ?)'
        self.conn.execute(query, params)

    def editar_protagonista(self, params):
        query = 'update protagoniza set titulo_pelicula = ?, año_pelicula = ?, nombre_estrella = ? where id = ?'
        self.conn.execute(query, params)

    def borrar_protagonista(self, id):
        query = 'delete from protagoniza where id = ?'
        self.conn.execute(query, params=[id])

    def ver_protagonistas(self):
        rows = self.conn.select('select id, titulo_pelicula, año_pelicula, nombre_estrella from protagoniza')
        protagonistas = []
        for fila in rows:
            protagonista = Protagoniza(fila[1], fila[2], fila[3], fila[0])
            protagonistas.append(protagonista)

        return protagonistas
