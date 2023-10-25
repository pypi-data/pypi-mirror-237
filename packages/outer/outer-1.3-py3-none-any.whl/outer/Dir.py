from outer.core.Path import Path
from outer.core.PathType import PathType
from outer.File import File


class Dir:
    def __init__(self, path: str):
        self.path = Path(path, path_type=PathType.DIR)

    def sub_dir(self, path: str):
        obj = self.path.sub(path, path_type=PathType.DIR)
        obj.create_dir()
        return Dir(obj)

    def sub_file(self, path: str):
        obj = self.path.sub(path, path_type=PathType.FILE)
        return File(obj)

    def __str__(self):
        return self.path.__str__()
