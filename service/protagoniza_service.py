class ProtagonizaService:

    def __init__(self, protagoniza_repository, pelicula_service, estrella_service):
        self.protagoniza_repository = protagoniza_repository
        self.pelicula_service = pelicula_service
        self.estrella_service = estrella_service

    def crear_protagonista(self):
        titulo_pelicula, año_pelicula, nombre_estrella = self.get_user_input()
        self.protagoniza_repository.crear_protagonista([titulo_pelicula, año_pelicula, nombre_estrella])
        print('Protagonista creado con éxito')

    def editar_protagonista(self):
        protagonistas = self.mostrar_protagonistas()

        id = input('Qué protagonista desea editar?\n')
        if id not in [str(protagonista.id) for protagonista in protagonistas]:
            print('Ingresó un id no válido')
            self.editar_protagonista()
        else:
            titulo_pelicula, año_pelicula, nombre_estrella = self.get_user_input()
            self.protagoniza_repository.editar_protagonista([titulo_pelicula, año_pelicula, nombre_estrella, id])
            print('Protagonista editado con éxito')

    def borrar_protagonista(self):
        protagonistas = self.mostrar_protagonistas()

        id = input('Qué protagonista desea borrar?\n')
        if id not in [str(protagonista.id) for protagonista in protagonistas]:
            print('Ingresó un id no válido')
            self.borrar_protagonista()
        else:
            self.protagoniza_repository.borrar_protagonista(id)
            print('Protagonista borrado con éxito')

    def ver_protagonistas(self):
        protagonistas = self.protagoniza_repository.ver_protagonistas()
        if len(protagonistas) == 0:
            print('No hay protagonistas existentes')
            return

        print('Protagonistas')
        for protagonista in protagonistas:
            print(f'\nTítulo: {protagonista.titulo_pelicula}\n'
                  f'Año: {protagonista.año_pelicula}\n'
                  f'Estrella: {protagonista.nombre_estrella}')

    def mostrar_protagonistas(self):
        protagonistas = self.protagoniza_repository.ver_protagonistas()
        if len(protagonistas) == 0:
            print('No hay protagonistas existentes')
            return

        for protagonista in protagonistas:
            print(f'\nId: {protagonista.id}\n'
                  f'Título: {protagonista.titulo_pelicula}\n'
                  f'Año: {protagonista.año_pelicula}\n'
                  f'Estrella: {protagonista.nombre_estrella}')

        return protagonistas

    def get_user_input(self):
        peliculas = self.pelicula_service.ver_peliculas_protagonistas()
        titulo_pelicula = ''
        año_pelicula = None
        nombre_estrella = ''
        if len(peliculas) == 0:
            print('No hay peliculas existentes')
        else:
            pelicula_id = input('Ingrese el id de la película\n')
            for pelicula in peliculas:
                if str(pelicula[0]) == pelicula_id:
                    titulo_pelicula = pelicula[1]
                    año_pelicula = pelicula[2]

        estrellas = self.estrella_service.mostrar_nombres_estrellas()
        if len(estrellas) == 0:
            print('No hay estrellas existentes')
        else:
            estrella_id = input('Ingrese el id de la estrella\n')
            for estrella in estrellas:
                if str(estrella[0]) == estrella_id:
                    nombre_estrella = estrella[1]

        return titulo_pelicula, año_pelicula, nombre_estrella
