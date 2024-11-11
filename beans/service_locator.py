class ServiceLocator:

    _services = {}

    @classmethod
    def register_service(cls, name, service):
        cls._services[name] = service

    @classmethod
    def get_service(cls, name):
        service = cls._services.get(name)
        if not service:
            raise ValueError(f'Service {name} not found')
        else:
            return service