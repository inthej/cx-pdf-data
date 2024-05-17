import os

from fastapi import HTTPException
from fastapi.responses import FileResponse

from exceptions import DirectoryNotFoundException, FileNotFoundException
from services import cx_service


async def get_dir_pdf_files(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        response = cx_service.get_dir_pdf_files(dir_path)
        return response
    except DirectoryNotFoundException as e:
        raise e
    except FileNotFoundException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def create_dir_pdf_to_excels(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        response = cx_service.create_pdf_to_excels(dir_path)
        return response
    except DirectoryNotFoundException as e:
        raise e
    except FileNotFoundException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def download_pdf(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        return FileResponse(path=pdf_path, filename="downloaded_file.pdf", media_type='application/pdf')
    except DirectoryNotFoundException as e:
        raise e
    except FileNotFoundException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
