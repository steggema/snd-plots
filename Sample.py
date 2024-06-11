from glob import glob
from dataclasses import dataclass

@dataclass
class Sample:
    name: str
    files: list
    process: str = ''
    xsec: float = 1.
    n_ev_produced: float = 1.
    class_select: int = -1

    def get_files(self) -> list:
        files = sum([glob(file) for file in self.files], [])
        return files