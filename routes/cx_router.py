from fastapi import APIRouter
from controllers import cx_controller
from urllib import parse

router = APIRouter(tags=["CX Services"])

@router.get("/cx/pdf/files", summary="디렉토리 pdf 파일 조회")
async def get_directory_pdf_files(dir_path: str):
    decoded_dir_path = parse.unquote(dir_path)
    return await cx_controller.get_dir_pdf_files(decoded_dir_path)


@router.post("/cx/pdf/to-excels", summary="디렉토리 내 PDF 파일을 Excel 파일로 생성")
async def create_pdf_to_excels(dir_path: str):
    decoded_dir_path = parse.unquote(dir_path)
    return await cx_controller.create_dir_pdf_to_excels(decoded_dir_path)

@router.get("/cx/pdf/download")
async def download_pdf(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await cx_controller.download_pdf(decoded_dir_path, decoded_filename)