import re

import fitz  # PyMuPDF
from konlpy.tag import Kkma
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

kkma = Kkma()


def extract_texts(pdf_path: str):
    try:
        result = []
        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                text = page.get_text()
                result.append({
                    "page_no": int(page_number),
                    "text": text
                })

            #print('length', len(result))
            return result
    except Exception as e:
        raise e


def extract_texts_by_page(pdf_path: str, page_no: int):
    try:
        result = None
        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                if page_number != page_no:
                    continue

                text = page.get_text()
                result = {
                    "page_no": int(page_number),
                    "text": text
                }

            #print('result', result)
            return result
    except Exception as e:
        raise e


def extract_texts_details_by_page(pdf_path: str, page_no: int):
    try:
        result = None
        with fitz.open(pdf_path) as doc:
            paragraphs_blocks = _get_paragraphs_blocks_by_page(pdf_path, page_no)  # 문단

            for page_number, page in enumerate(doc, start=1):
                if page_number != page_no:
                    continue

                text = page.get_text()
                #morphs = kkma.morphs(text)  # 형태소 추출
                #nouns = kkma.nouns(text)  # 명사 추출

                paragraphs = _get_paragraphs(text)  # 문단
                sentences = kkma.sentences(text)  # 문장
                #sentences = _get_sentences(paragraphs_blocks)  # 문장

                result = {
                    "page_no": int(page_number),
                    #"text": text,
                    #"paragraphs": paragraphs,
                    "paragraphs_blocks": paragraphs_blocks,
                    "sentences": sentences,
                    #"morphs": morphs,
                    #"nouns": nouns
                }

            #print('result', result)
            return result
    except Exception as e:
        raise e


def extract_paragraphs(pdf_path: str):
    try:
        result = _get_paragraphs_blocks(pdf_path)  # 문단
        return result
    except Exception as e:
        raise e
    
def extract_paragraphs_by_page(pdf_path: str, page_no: int):
    try:
        result = _get_paragraphs_blocks_by_page(pdf_path, page_no)  # 문단
        return result
    except Exception as e:
        raise e
    
def extract_sentences(pdf_path: str):
    try:
        result = []
        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                text = page.get_text()
                sentences = kkma.sentences(text)
                
                result.append({
                    "page_no": page_number,
                    "texts": sentences
                })
            return result
    except Exception as e:
        raise e
    
    
def extract_sentences_by_page(pdf_path: str, page_no: int):
    try:
        result = None
        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                if page_number != page_no:
                    continue
                
                text = page.get_text()
                sentences = kkma.sentences(text)
                
                result = {
                    "page_no": page_number,
                    "texts": sentences
                }
            return result
    except Exception as e:
        raise e    


# 문단 추출
def _get_paragraphs(text):
    paragraphs = re.split(r'(?=\n\d+\n)|(?=\n\n)', text.strip())  # 정규 표현식 사용 '\n숫자\n' 패턴을 찾아 이를 기준으로 문단을 나눈다
    paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]  # 빈 문자열 제거
    return paragraphs


# 문단 블록 추출: 좌표 정보로 텍스트를 묶음
def _get_paragraphs_blocks(pdf_path):
    pages_texts = []
    for page_number, page_layout in enumerate(extract_pages(pdf_path), start=1):
        result = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text().strip()
                if text:
                    result.append(text)

        pages_texts.append({
            "page_no": page_number,
            "paragraphs": result
        })
    return pages_texts


# 문단 블록 추출 By 페이지: 좌표 정보로 텍스트를 묶음
def _get_paragraphs_blocks_by_page(pdf_path, page_no):
    pages_text = []
    for page_number, page_layout in enumerate(extract_pages(pdf_path), start=1):
        if page_no != page_number:
            continue

        for element in page_layout:
            if isinstance(element, LTTextContainer):
                pages_text.append(element.get_text().strip())
    return pages_text


# 문장 추출
def _get_sentences(paragraphs: []):
    result = []
    for paragraph in paragraphs:
        sentences = kkma.sentences(paragraph)
        for sentence in sentences:
            result.append(sentence)
    return result


"""
# 문장 추출
def _get_sentences(text):
    pattern = r'(?<=[.!?])\s+' # 마침표, 물음표, 느낌표 다음에 공백이 오는 경우에만 문장으로 인식
    sentences = re.split(pattern, text.strip())  # 지정한 패턴을 사용하여 문장을 분리합니다.
    sentences = [sentence.strip().replace('\n', ' ') for sentence in sentences if sentence.strip()]  # 줄바꿈을 공백으로 대체하고 빈 문자열 제거
    return sentences
"""


def extract_links_with_text(pdf_path: str):
    try:
        with fitz.open(pdf_path) as doc:
            result = []
            for page_number, page in enumerate(doc, start=1):
                text_instances = page.get_text("words")  # 현재 페이지 텍스트 단어 추출
                links = page.get_links()
                for link in links:
                    if link['kind'] == fitz.LINK_NAMED:  # 내부 페이지 링크 확인
                        link_texts = _find_text_by_intersection(link['from'], text_instances)
                        if len(link_texts):
                            result.append({
                                "link_texts": link_texts,
                                "page_no": page_number,
                                "to_page": int(link['page'])
                            })

            #print('length', len(result))
            return result
    except Exception as e:
        raise e


def extract_links_with_text_by_page(pdf_path: str, page_no: int):
    try:
        with fitz.open(pdf_path) as doc:
            result = []
            for page_number, page in enumerate(doc, start=1):
                if page_number != page_no:
                    continue

                text_instances = page.get_text("words")  # 현재 페이지 텍스트 단어 추출
                links = page.get_links()
                #print(links)
                for link in links:
                    if link['kind'] == fitz.LINK_NAMED:  # 내부 페이지 링크 확인
                        link_texts = _find_text_by_intersection(link['from'], text_instances)
                        result.append({
                            "link_texts": link_texts,
                            "page_no": page_number,
                            "to_page": int(link['page'])
                        })

            return result
    except Exception as e:
        raise e


# 목차 추출
def extract_outlines(pdf_path: str):
    try:
        # PDF 파일 열기
        with fitz.open(pdf_path) as doc:
            # 목차(북마크) 정보 추출
            bookmarks = doc.get_toc(simple=False)
            result = []
            for index, bookmark in enumerate(bookmarks, start=1):
                level, title, page, details = bookmark
                page_number = details.get('page')
                result.append({
                    "level": level,
                    "title": title,
                    "to_page": int(page_number)
                })

            #print('length', len(result))
            return result
    except Exception as e:
        raise e


def _find_text_by_intersection(link_rect, words):
    link_area = fitz.Rect(link_rect)  # 링크 좌표를 사각형으로 변환(교차점 확인을 위한 Rect로 변환)
    linked_texts = []
    for word in words:
        word_rect = fitz.Rect(word[:4])  # 단어의 사각형 영역 만들기
        #print('word', word[4])
        #print('word_rect', word_rect)
        #print('link_area', link_area)
        if word_rect.intersects(link_area):  # 단어의 영역이 링크의 영역과 교차하는지 확인
            linked_texts.append(word[4])
    return linked_texts
