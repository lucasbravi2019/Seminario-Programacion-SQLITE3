from beans.service_locator import ServiceLocator
from database.db import Database
from menu.estrella_menu import EstrellaMenu
from menu.estudio_menu import EstudioMenu
from menu.menu_inicial import MenuInicial
from menu.pelicula_menu import PeliculaMenu
from menu.protagoniza_menu import ProtagonizaMenu
from repository.estrella_repository import EstrellaReposository
from repository.estudio_repository import EstudioRepository
from repository.pelicula_repository import PeliculaRepository
from repository.protagoniza_repository import ProtagonizaRepository
from service.estrella_service import EstrellaService
from service.estudio_service import EstudioService
from service.pelicula_service import PeliculaService
from service.protagoniza_service import ProtagonizaService

MENU = 'menu'

CONN = 'conn'

ESTUDIO = 'estudio'

ESTRELLA = 'estrella'

PROTAGONIZA = 'protagoniza'

PELICULA = 'pelicula'


class BeanFactory:

    @classmethod
    def init_beans(cls):
        ServiceLocator.register_service(CONN, Database())
        database = ServiceLocator.get_service(CONN)
        estudio_service = EstudioService(EstudioRepository(database))
        pelicula_service = PeliculaService(PeliculaRepository(database), estudio_service)
        estrella_service = EstrellaService(EstrellaReposository(database))
        ServiceLocator.register_service(PROTAGONIZA, ProtagonizaService(ProtagonizaRepository(database),
                                                                        pelicula_service, estrella_service))
        ServiceLocator.register_service(ESTRELLA, estrella_service)
        ServiceLocator.register_service(ESTUDIO, estudio_service)
        ServiceLocator.register_service(PELICULA, pelicula_service)

    def __init__(self):
        BeanFactory.init_beans()
        pelicula_service = ServiceLocator.get_service(PELICULA)
        protagoniza_service = ServiceLocator.get_service(PROTAGONIZA)
        estrella_service = ServiceLocator.get_service(ESTRELLA)
        estudio_service = ServiceLocator.get_service(ESTUDIO)
        self.services = {PELICULA: pelicula_service, PROTAGONIZA: protagoniza_service, ESTRELLA: estrella_service,
                         ESTUDIO: estudio_service}
        self.menu = MenuInicial(PeliculaMenu(pelicula_service), EstrellaMenu(estrella_service),
                                EstudioMenu(estudio_service), ProtagonizaMenu(protagoniza_service))

    def get_pelicula_service(self):
        return self.services[PELICULA]

    def get_protagoniza_service(self):
        return self.services[PROTAGONIZA]

    def get_estudio_service(self):
        return self.services[ESTUDIO]

    def get_estrella_service(self):
        return self.services[ESTRELLA]

    def get_menu(self):
        return self.menu