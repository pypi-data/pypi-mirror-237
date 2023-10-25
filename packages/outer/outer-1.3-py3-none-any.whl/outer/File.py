from outer.core.Path import Path
from outer.core.PathType import PathType


class File:
    def __init__(self, path: str):
        self.path = Path(path, path_type=PathType.FILE)

    def __str__(self):
        return self.path.__str__()