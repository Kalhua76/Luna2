from dataclasses import dataclass, field
from typing import Type

@dataclass
class ServiceDescriptor:
    name:str
    service_type:Type
    instance:object
    dependencies:list[str]=field(default_factory=list)
    initialized:bool=False
