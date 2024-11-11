class ProtagonizaMenu:

    def __init__(self, protagoniza_service):
        self.protagoniza_service = protagoniza_service
        self.acciones = {'1': self.protagoniza_service.crear_protagonista, '2': self.protagoniza_service.editar_protagonista,
                         '3': self.protagoniza_service.borrar_protagonista, '4': self.protagoniza_service.ver_protagonistas}

    def mostrar_menu(self):
        print('Qué acción desea realizar?')
        print('1. Crear Protagonista')
        print('2. Editar Protagonista')
        print('3. Borrar Protagonista')
        print('4. Ver todos los Protagonistas')
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