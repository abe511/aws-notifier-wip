
from abc import ABC
from dataclasses import dataclass

@dataclass
class EnvItemEntity(ABC):
    key: str
    value: str


@dataclass
class EventEntity(ABC):
    body: str
    to: str
    event_type: tuple = ("new_publication", "approved_publication")

print(dir(EventEntity))
