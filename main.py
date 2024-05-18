from fastapi import FastAPI

from exceptions import DirectoryNotFoundException, FileNotFoundException, ServerErrorException
from handlers import directory_not_found_exception_handler, file_not_found_exception_handler, server_error_exception_handler
from routes.cx_router import router as cx_router
from routes.pdf_router import router as pdf_router

app = FastAPI()

# routers
app.include_router(pdf_router)
app.include_router(cx_router)

# exception handlers
app.add_exception_handler(DirectoryNotFoundException, directory_not_found_exception_handler)
app.add_exception_handler(FileNotFoundException, file_not_found_exception_handler)
app.add_exception_handler(ServerErrorException, server_error_exception_handler)


@app.get("/")
async def home():
    return {"message": "Hello World"}


"""
    if __name__ == '__main__':
        uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
"""
