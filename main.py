from fastapi import FastAPI
from routes.pdf_router import router as pdf_router
from routes.cx_router import router as cx_router
import uvicorn

app = FastAPI()

app.include_router(pdf_router)
app.include_router(cx_router)


@app.get("/")
async def home():
    return {"message": "Hello World"}


"""
    if __name__ == '__main__':
        uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
"""
