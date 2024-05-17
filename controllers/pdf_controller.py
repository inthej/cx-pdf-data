import os

from fastapi import HTTPException
from services import pdf_service


async def get_texts(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_texts(pdf_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}


async def get_texts_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_texts_by_page(pdf_path, page_no)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}


async def get_texts_details_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_texts_details_by_page(pdf_path, page_no)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}


async def get_paragraphs(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_paragraphs(pdf_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}
    

async def get_paragraphs_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_paragraphs_by_page(pdf_path, page_no)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}

    
async def get_sentences(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_sentences(pdf_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}    
    
    
async def get_sentences_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_sentences_by_page(pdf_path, page_no)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}        


async def get_links(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_links_with_text(pdf_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}


async def get_links_by_page(dir_path: str, filename: str, page_no: int):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_links_with_text_by_page(pdf_path, page_no)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}
    
    
async def get_outlines(dir_path: str, filename: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        # PDF FILE PATH
        pdf_path = os.path.join(os.getcwd(), dir_path, filename)
        
        if not os.path.isfile(pdf_path):
            raise HTTPException(status_code=404, detail="File Not Found Exception")
        
        response = pdf_service.extract_outlines(pdf_path)
        return {"code": 200, "success": True, "obj": response}
    except Exception as e:
        return {"code": 500, "success": False, "message": '서버 에러', "error": str(e)}

