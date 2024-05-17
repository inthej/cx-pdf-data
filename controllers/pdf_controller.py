import os

from fastapi import HTTPException

from exceptions import DirectoryNotFoundException, FileNotFoundException
from services import pdf_service


async def get_texts(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_texts(pdf_path)
        return response
    except DirectoryNotFoundException as e:
        raise e
    except FileNotFoundException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_texts_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_texts_by_page(pdf_path, page_no)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_texts_details_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_texts_details_by_page(pdf_path, page_no)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_paragraphs(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_paragraphs(pdf_path)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_paragraphs_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_paragraphs_by_page(pdf_path, page_no)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_sentences(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_sentences(pdf_path)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_sentences_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_sentences_by_page(pdf_path, page_no)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_links(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_links_with_text(pdf_path)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_links_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_links_with_text_by_page(pdf_path, page_no)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_outlines(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise DirectoryNotFoundException(404, dir_path)

        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundException(404, filename)

        response = pdf_service.extract_outlines(pdf_path)
        return response
    except DirectoryNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except FileNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
