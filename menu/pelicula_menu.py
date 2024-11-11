class PeliculaMenu:

    def __init__(self, pelicula_service):
        self.pelicula_service = pelicula_service
        self.acciones = {'1': self.pelicula_service.crear_pelicula, '2': self.pelicula_service.editar_pelicula,
                         '3': self.pelicula_service.borrar_pelicula, '4': self.pelicula_service.ver_peliculas}

    def mostrar_menu(self):
        print('Qué acción desea realizar?')
        print('1. Crear Película')
        print('2. Editar Película')
        print('3. Borrar Película')
        print('4. Ver todas las películas')
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
