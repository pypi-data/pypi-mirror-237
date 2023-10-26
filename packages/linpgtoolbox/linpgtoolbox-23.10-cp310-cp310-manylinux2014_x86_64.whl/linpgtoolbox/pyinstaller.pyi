from typing import Final

class PyInstaller:
    __FOLDER: Final[str]
    @classmethod
    def generate(cls, _name: str, _path: str, _hidden_imports: list[str]) -> None: ...
