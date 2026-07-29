from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def initialize(self): ...
    @abstractmethod
    def shutdown(self): ...
