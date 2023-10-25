import os

from outer.core.PathType import PathType


class Path:
    def __init__(self, path: str, path_type: PathType = PathType.DIR):
        self.root = None
        self.path = path
        self.path_type = path_type
        self.args = None

    def sub(self, path: str, path_type: PathType = PathType.DIR):
        path_obj = Path(path, path_type=path_type)
        path_obj.root = self
        return path_obj

    def create_dir(self, *args):
        self.args = args
        if self.path_type.value == PathType.DIR.value:
            path_to_create = self.__str__().format(*args)
            os.makedirs(path_to_create, exist_ok=True)
        elif self.root is not None:
            self.root.create_dir(*args)
        return self

    def __str__(self):
        out_path = self.path.__str__() if self.root is None else os.path.join(self.root.__str__(), self.path.__str__())

        if self.args is not None and len(self.args) > 0:
            print(self.args)
            return out_path.format(*self.args)
        else:
            return out_path


