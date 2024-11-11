class EstudioService:

    def __init__(self, estudio_repository):
        self.estudio_repository = estudio_repository

    def crear_estudio(self):
        nombre, direccion = self.get_user_input()
        self.estudio_repository.crear_estudio([nombre, direccion])
        print('Estudio creado con éxito')

    def editar_estudio(self):
        estudios = self.mostrar_nombres_estudios()

        id = input('Qué película desea editar?\n')
        if id not in [str(estudio[0]) for estudio in estudios]:
            print('Ingresó un id no válido')
            self.editar_estudio()
        else:
            nombre, direccion = self.get_user_input()
            self.estudio_repository.editar_estudio([nombre, direccion, id])
            print('Estudio editado con éxito')

    def borrar_estudio(self):
        estudios = self.mostrar_nombres_estudios()

        id = input('Qué estudio desea borrar?\n')
        if id not in [str(estudio[0]) for estudio in estudios]:
            print('Ingresó un id no válido')
            self.borrar_estudio()
        else:
            self.estudio_repository.borrar_estudio(id)
            print('Estudio borrado con éxito')

    def ver_estudios(self):
        estudios = self.estudio_repository.ver_estudios()
        print('Estudios')
        for estudio in estudios:
            print(f'\nNombre: {estudio.nombre}\n'
                  f'Dirección: {estudio.direccion}')

    def get_user_input(self):
        nombre = input('Ingrese el nombre del estudio\n')
        direccion = input('Ingrese la dirección del estudio\n')
        return nombre, direccion

    def mostrar_nombres_estudios(self):
        estudios = self.estudio_repository.ver_nombres_estudios()
        for estudio in estudios:
            print(f'Id: {estudio[0]}, Nombre: {estudio[1]}')

        return estudios
