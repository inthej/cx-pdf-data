import os

from services import pdf_service
from fastapi import HTTPException

def get_dir_pdf_files(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")

        # 디렉토리 내의 모든 파일 나열
        files = os.listdir(dir_path)
        pdf_files = list(filter(lambda file: os.path.splitext(file)[1] == '.pdf', files))
        
        return pdf_files

    except Exception as e:
        raise e
    
    
def create_pdf_to_excels(dir_path: str):
    try:
        if not os.path.isdir(dir_path):
            raise HTTPException(status_code=404, detail="Directory Path Not Found Exception")
        
        response = []
        files = os.listdir(dir_path)
        for file_index, file in enumerate(files):
            filename = os.path.splitext(file)[0] + os.path.splitext(file)[1]
            pdf_path = os.path.join(os.getcwd(), dir_path, filename)
            texts_response = pdf_service.extract_paragraphs(pdf_path)
            response.append({
                "file_idx": file_index,
                "filename": filename,
                "texts": texts_response
            })
            
        return response
    except Exception as e:
        raise e