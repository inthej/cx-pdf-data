from fastapi.requests import Request
from fastapi.responses import JSONResponse

from exceptions import ServerErrorException


async def server_error_exception_handler(request: Request, exc: ServerErrorException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "success": False,
            "message": "서버 에러",
            "error": exc.detail
        }
    )
