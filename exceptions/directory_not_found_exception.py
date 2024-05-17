from fastapi import HTTPException


class DirectoryNotFoundException(HTTPException):
    def __init__(self, code: int, dir_path: str):
        super().__init__(status_code=code, detail=f"Directory path '{dir_path}' not found")
