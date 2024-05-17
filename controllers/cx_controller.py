import os

from fastapi import HTTPException
from services import cx_pdf_service
from fastapi.responses import FileResponse

async def get_dir_pdf_files(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        response = cx_pdf_service.get_dir_pdf_files(dir_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}
    
    
async def create_dir_pdf_to_excels(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")

        response = cx_pdf_service.create_pdf_to_excels(dir_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}
    
    
async def download_pdf(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        return FileResponse(path=pdf_path, filename="downloaded_file.pdf", media_type='application/pdf')
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}    