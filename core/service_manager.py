from __future__ import annotations
from typing import Any
from core.service_descriptor import ServiceDescriptor
from core.exceptions import ServiceAlreadyRegistered, ServiceNotFound

class ServiceManager:
    def __init__(self):
        self._services:dict[str,ServiceDescriptor]={}

    def register(self,name:str,service:object,dependencies:list[str]|None=None):
        if name in self._services:
            raise ServiceAlreadyRegistered(name)
        self._services[name]=ServiceDescriptor(name,type(service),service,dependencies or [])

    def get(self,name:str)->Any:
        if name not in self._services:
            raise ServiceNotFound(name)
        return self._services[name].instance

    def exists(self,name:str):
        return name in self._services

    def initialize_all(self):
        initialized=set()
        while len(initialized)<len(self._services):
            progress=False
            for d in self._services.values():
                if d.initialized:
                    continue
                if all(dep in initialized for dep in d.dependencies):
                    d.instance.initialize()
                    d.initialized=True
                    initialized.add(d.name)
                    progress=True
            if not progress:
                raise RuntimeError("Impossible de résoudre les dépendances des services.")

    def shutdown_all(self):
        for d in reversed(list(self._services.values())):
            if d.initialized:
                d.instance.shutdown()
                d.initialized=False

    def clear(self):
        self._services.clear()

    def list_services(self):
        return list(self._services.keys())
