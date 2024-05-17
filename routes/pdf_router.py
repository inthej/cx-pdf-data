from fastapi import APIRouter
from controllers import pdf_controller
from urllib import parse

router = APIRouter(tags=["PDF Services"])


@router.get("/pdf/texts", summary="전체 텍스트")
async def pdf_texts(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_texts(decoded_dir_path, decoded_filename)


@router.get("/pdf/page/{page_no}/texts", summary="페이지 텍스트")
async def pdf_texts_by_page(dir_path: str, filename: str, page_no: int):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_texts_by_page(decoded_dir_path, decoded_filename, page_no)


@router.get("/pdf/page/{page_no}/texts/details", summary="페이지 텍스트 세부사항")
async def pdf_texts_details_by_page(dir_path: str, filename: str, page_no: int):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_texts_details_by_page(decoded_dir_path, decoded_filename, page_no)


@router.get("/pdf/paragraphs", summary="전체 문단")
async def pdf_paragraphs(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_paragraphs(decoded_dir_path, decoded_filename)

@router.get("/pdf/{page_no}/paragraphs", summary="페이지 문단")
async def pdf_paragraphs(dir_path: str, filename: str, page_no: int):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_paragraphs_by_page(decoded_dir_path, decoded_filename, page_no)


@router.get("/pdf/sentences", summary="전체 문장")
async def pdf_sentences(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_sentences(decoded_dir_path, decoded_filename)


@router.get("/pdf/page/{page_no}/sentences", summary="페이지 문장")
async def pdf_sentences_by_page(dir_path: str, filename: str, page_no: int):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_sentences_by_page(decoded_dir_path, decoded_filename, page_no)


@router.get("/pdf/links", summary="전체 링크")
async def pdf_links(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_links(decoded_dir_path, decoded_filename)


@router.get("/pdf/page/{page_no}/links", summary="페이지 링크")
async def pdf_link(dir_path: str, filename: str, page_no: int):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_links_by_page(decoded_dir_path, decoded_filename, page_no)


@router.get("/pdf/outlines", summary="목차 목록")
async def pdf_outlines(dir_path: str, filename: str):
    decoded_dir_path = parse.unquote(dir_path)
    decoded_filename = parse.unquote(filename)
    return await pdf_controller.get_outlines(decoded_dir_path, decoded_filename)

