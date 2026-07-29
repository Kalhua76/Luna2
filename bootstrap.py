from core.service_manager import ServiceManager

class Bootstrap:
    def __init__(self):
        self.service_manager=ServiceManager()

    def register_services(self):
        # Les services seront enregistrés ici
        pass

    def start(self):
        self.register_services()
        self.service_manager.initialize_all()

    def stop(self):
        self.service_manager.shutdown_all()
