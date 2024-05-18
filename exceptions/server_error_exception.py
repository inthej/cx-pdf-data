from fastapi import HTTPException


class ServerErrorException(HTTPException):
    def __init__(self, code: int = 500, detail: str = "Internal Server Error"):
        super().__init__(status_code=code, detail=detail)
