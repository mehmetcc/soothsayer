from pathlib import Path


class FileUtils:
    @staticmethod
    def get_parent(p: str) -> str:
        return str(Path(p).resolve().parent)

    @staticmethod
    def get_caller_parent() -> str:
        return FileUtils.get_parent(FileUtils.get_parent(__file__))
