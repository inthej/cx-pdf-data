from fastapi import HTTPException


class FileNotFoundException(HTTPException):
    def __init__(self, status_code: int, filename: str):
        super().__init__(status_code=status_code, detail=f"File '{filename}' not found")
