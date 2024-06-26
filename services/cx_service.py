import os

from services import pdf_service


def get_dir_pdf_files(dir_path: str):
    try:
        files = os.listdir(dir_path)
        pdf_files = list(filter(lambda file: os.path.splitext(file)[1].lower().endswith('.pdf'), files))

        return pdf_files

    except Exception as e:
        raise e


def create_pdf_to_excels(dir_path: str):
    try:
        response = []
        listdir = os.listdir(dir_path)
        files = [file_name for file_name in listdir if file_name.lower().endswith('.pdf')]
        for file_index, file in enumerate(files):
            filename = os.path.splitext(file)[0] + os.path.splitext(file)[1]
            pdf_path = os.path.join(os.getcwd(), dir_path, filename)
            paragraphs = pdf_service.extract_paragraphs(pdf_path)
            response.append({
                "file_idx": file_index,
                "filename": filename,
                "texts": paragraphs
            })

        return response
    except Exception as e:
        raise e
