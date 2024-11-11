class EstudioMenu:

    def __init__(self, estudio_service):
        self.estudio_service = estudio_service
        self.acciones = {'1': self.estudio_service.crear_estudio, '2': self.estudio_service.editar_estudio,
                         '3': self.estudio_service.borrar_estudio, '4': self.estudio_service.ver_estudios}

    def mostrar_menu(self):
        print('Qué acción desea realizar?')
        print('1. Crear Estudio')
        print('2. Editar Estudio')
        print('3. Borrar Estudio')
        print('4. Ver todos los estudios')
        print('5. Salir')
        opcion = input()

        if opcion == '5':
            return

        accion = self.acciones.get(opcion)
        if accion is None:
            print('Ingresó una opción inválida, por favor intente nuevamente')
            self.mostrar_menu()
        else:
            accion()
            self.mostrar_menu()