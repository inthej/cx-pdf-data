from fastapi import HTTPException


class DirectoryNotFoundException(HTTPException):
    def __init__(self, status_code: int, dir_path: str):
        super().__init__(status_code=status_code, detail=f"Directory path '{dir_path}' not found")
