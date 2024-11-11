from entity.pelicula import Pelicula


class PeliculaRepository:

    def __init__(self, conn):
        self.conn = conn

    def crear_pelicula(self, params):
        query = 'insert into pelicula (titulo, año, duracion, nombre_estudio) values (?, ?, ?, ?)'
        self.conn.execute(query, params)

    def editar_pelicula(self, params):
        query = 'update pelicula set titulo = ?, año = ?, duracion = ?, nombre_estudio = ? where id = ?'
        self.conn.execute(query, params)

    def borrar_pelicula(self, id):
        query = 'delete from pelicula where id = ?'
        self.conn.execute(query, params=[id])

    def ver_peliculas(self):
        rows = self.conn.select('select id, titulo, año, duracion, nombre_estudio from pelicula')
        peliculas = []
        for fila in rows:
            pelicula = Pelicula(fila[1], fila[2], fila[3], fila[4], fila[0])
            peliculas.append(pelicula)

        return peliculas

    def ver_titulos_peliculas(self):
        rows = self.conn.select('select id, titulo from pelicula')
        peliculas = []
        for fila in rows:
            pelicula = (fila[0], fila[1])
            peliculas.append(pelicula)

        return peliculas

    def ver_peliculas_protagonistas(self):
        rows = self.conn.select('select id, titulo, año from pelicula')
        peliculas = []
        for fila in rows:
            pelicula = (fila[0], fila[1], fila[2])
            peliculas.append(pelicula)

        return peliculas