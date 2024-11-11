class MenuInicial:

    def __init__(self, pelicula_menu, estrella_menu, estudio_menu, protagoniza_menu):
        self.pelicula_menu = pelicula_menu
        self.estrella_menu = estrella_menu
        self.estudio_menu = estudio_menu
        self.protagoniza_menu = protagoniza_menu
        self.acciones = {'1': self.pelicula_menu.mostrar_menu, '2': self.estrella_menu.mostrar_menu,
                         '3': self.estudio_menu.mostrar_menu, '4': self.protagoniza_menu.mostrar_menu}

    def mostrar_menu(self):
        print('Bienvenido')
        print('A qué sección desea ingresar?')
        print('1. Peliculas')
        print('2. Estrellas')
        print('3. Estudios')
        print('4. Protagonistas')
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