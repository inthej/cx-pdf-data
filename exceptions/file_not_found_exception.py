from fastapi import HTTPException


class FileNotFoundException(HTTPException):
    def __init__(self, code: int, filename: str):
        super().__init__(status_code=code, detail=f"File '{filename}' not found")
