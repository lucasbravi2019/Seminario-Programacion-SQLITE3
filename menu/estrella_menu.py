class EstrellaMenu:

    def __init__(self, estrella_service):
        self.estrella_service = estrella_service
        self.acciones = {'1': self.estrella_service.crear_estrella, '2': self.estrella_service.editar_estrella,
                         '3': self.estrella_service.borrar_estrella, '4': self.estrella_service.ver_estrellas}

    def mostrar_menu(self):
        print('Qué acción desea realizar?')
        print('1. Crear Estrella')
        print('2. Editar Estrella')
        print('3. Borrar Estrella')
        print('4. Ver todas las estrellas')
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