class PeliculaService:

    def __init__(self, pelicula_repository, estudio_service):
        self.pelicula_repository = pelicula_repository
        self.estudio_service = estudio_service

    def crear_pelicula(self):
        año, duracion, nombre_estudio, titulo = self.get_user_input()
        self.pelicula_repository.crear_pelicula([titulo, año, duracion, nombre_estudio])
        print('Película creada con éxito')

    def editar_pelicula(self):
        peliculas = self.mostrar_titulos_peliculas()

        id = input('Qué película desea editar?\n')
        if id not in [str(pelicula[0]) for pelicula in peliculas]:
            print('Ingresó un id no válido')
            self.editar_pelicula()
        else:
            año, duracion, nombre_estudio, titulo = self.get_user_input()
            self.pelicula_repository.editar_pelicula([titulo, año, duracion, nombre_estudio, id])
            print('Película editada con éxito')

    def borrar_pelicula(self):
        peliculas = self.mostrar_titulos_peliculas()

        id = input('Qué película desea borrar?\n')
        if id not in [str(pelicula[0]) for pelicula in peliculas]:
            print('Ingresó un id no válido')
            self.borrar_pelicula()
        else:
            self.pelicula_repository.borrar_pelicula(id)
            print('Película borrada con éxito')

    def ver_peliculas(self):
        peliculas = self.pelicula_repository.ver_peliculas()
        print('Peliculas')
        for pelicula in peliculas:
            print(f'\nTítulo: {pelicula.titulo}\n'
                  f'Año: {pelicula.año}\n'
                  f'Duración: {pelicula.duracion} hs\n'
                  f'Estudio: {pelicula.nombre_estudio}')

    def mostrar_titulos_peliculas(self):
        peliculas = self.pelicula_repository.ver_titulos_peliculas()
        for pelicula in peliculas:
            print(f'Id: {pelicula[0]}, Título: {pelicula[1]}')

        return peliculas

    def ver_peliculas_protagonistas(self):
        peliculas = self.pelicula_repository.ver_peliculas_protagonistas()
        for pelicula in peliculas:
            print(f'Id: {pelicula[0]}, Título: {pelicula[1]}')

        return peliculas

    def get_user_input(self):
        titulo = input('Ingrese el título de la película\n')
        año = input('Ingrese el año de la película\n')
        duracion = input('Ingrese la duración de la película\n')
        estudios = self.estudio_service.mostrar_nombres_estudios()
        nombre_estudio = ''
        if len(estudios) == 0:
            print('No hay estudios existentes')
        else:
            estudio_id = input('Ingrese el id del estudio perteneciente a la película\n')
            for estudio in estudios:
                if str(estudio[0]) == estudio_id:
                    nombre_estudio = estudio[1]

        return año, duracion, nombre_estudio, titulo