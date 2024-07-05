from dataclasses import dataclass
from typing import Callable

@dataclass
class Var:
    name: str
    func: Callable
    title: str = ''
    unit: str = ''
