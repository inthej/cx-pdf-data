from fastapi.requests import Request
from fastapi.responses import JSONResponse

from exceptions import DirectoryNotFoundException


async def directory_not_found_exception_handler(request: Request, exc: DirectoryNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "success": False,
            "message": exc.detail,
            "error": "Directory path not found"
        }
    )
