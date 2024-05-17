from fastapi.requests import Request
from fastapi.responses import JSONResponse

from exceptions import FileNotFoundException


async def file_not_found_exception_handler(request: Request, exc: FileNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "success": False,
            "message": exc.detail,
            "error": "File not found"
        }
    )
