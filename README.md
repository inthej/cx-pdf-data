# cx-pdf-data
PDF 데이터 추출 프로젝트

## 설치
```
$ pip install fastapi
$ pip install uvicorn
$ pip install PyMuPDF


# test
$ pip install konlpy
$ pip install nltk
$ pip install pdfminer.six

```

## References
- KoNLPy(코엔엘파이) 형태소 토크나이징: [https://seokii.tistory.com/28]
- 토크나이징 성능 비교: [https://m.blog.naver.com/j7youngh/222875104191])
- Kkma(꼬꼬마): [http://kkma.snu.ac.kr/]
- 파이썬 정규식: [https://wikidocs.net/4308]


## Start
```
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Update 
```
$ python -m pip install --upgrade pip # (파이썬 및 pip 업데이트)
$ pip install --upgrade setuptools wheel # 빌드 도구 
```

## API Test 
```
$ http://127.0.0.1:8000/docs
```

## Memo
FastAPI
- 웹 프레임워크, 비동기 처리 지원, Swagger 문서 자동 생성

Uvicorn
- ASGI(Asynchronous Server Gateway Interface) 비동기웹서버
- async / await 구문을 사용

파이뮤(PyMuPDF)
- 고급 전자 문서 처리 라이브러리, 다양한 문서 처리 기능 제공
- 텍스트, 이미지, 표 등의정보를 추출

sent_tokenize
- 텍스트 문장 분리

re
- 정규 표현식 모듈

nltk
- 자연어처리
- 텍스트에서 의미있는 정보 분석, 추출하고 이해하는 기술집합

konlpy
- 여러가지 형태소 분석기 제공 라이브러리
1) Kkma(꼬꼬마): 서울대학교 연구실에서 개발한 형태소 분석기
2) Okt: 트위터에서 개발한 형태소 분석기

pdfminer
- pdf 문서의 텍스트, 이미지 데이터추출 라이브러리
- 위치 정보를 기반으로 텍스트 블록을 식별할 수 있음


### 용어
형태소
- '가진 가장 작은 말의 단위' 로 더 이상 나누면 뜻이 없어짐

토큰(token)
- 가장 기본이 되는 단어

토크나이징(tokenizing)
- 텍스트 정보를 단위별로 나누는 것

어간
- 활용어가 활용할 때에 변하지 않는 부분

어절
- 문장을 구성하고 있는 각각의 마디
