from database.db import estudio


class EstrellaService:

    def __init__(self, estrella_repository):
        self.estrella_repository = estrella_repository

    def crear_estrella(self):
        nombre, direccion, sexo, fecha_nacimiento = self.get_user_input()
        self.estrella_repository.crear_estrella([nombre, direccion, sexo, fecha_nacimiento])
        print('Estrella creada con éxito')

    def editar_estrella(self):
        estrellas = self.mostrar_nombres_estrellas()

        id = input('Qué estrella desea editar?\n')
        if id not in [str(estrella[0]) for estrella in estrellas]:
            print('Ingresó un id no válido')
            self.editar_estrella()
        else:
            nombre, direccion, sexo, fecha_nacimiento = self.get_user_input()
            self.estrella_repository.editar_estrella([nombre, direccion, sexo, fecha_nacimiento, id])
            print('Estrella editada con éxito')

    def borrar_estrella(self):
        estrellas = self.mostrar_nombres_estrellas()

        id = input('Qué estrella desea borrar?\n')
        if id not in [str(estrella[0]) for estrella in estrellas]:
            print('Ingresó un id no válido')
            self.borrar_estrella()
        else:
            self.estrella_repository.borrar_estrella(id)
            print('Estrella borrada con éxito')

    def ver_estrellas(self):
        estrellas = self.estrella_repository.ver_estrellas()
        if len(estrellas) == 0:
            print('No hay estrellas')
            return

        print('Estrellas')
        for estrella in estrellas:
            print(f'\nNombre: {estrella.nombre}\n'
                  f'Dirección: {estrella.direccion}\n'
                  f'Sexo: {estrella.sexo}\n'
                  f'Fecha de nacimiento: {estrella.fecha_nacimiento}')

    def get_user_input(self):
        nombre = input('Ingrese el nombre de la estrella\n')
        direccion = input('Ingrese la dirección de la estrella\n')
        sexo = input('Ingrese el sexo de la estrella\n')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento de la estrella (yyyy-MM-dd)\n')
        return nombre, direccion, sexo, fecha_nacimiento

    def mostrar_nombres_estrellas(self):
        estrellas = self.estrella_repository.ver_nombres_estrellas()
        for estrella in estrellas:
            print(f'Id: {estrella[0]}, Nombre: {estrella[1]}')

        return estrellas