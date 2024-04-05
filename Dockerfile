FROM python:3.11-alpine3.19

# 필요한 패키지 설치
RUN pip install django

RUN apk add --no-cache mariadb-dev
RUN apk add --no-cache build-base mariadb-dev

# 작업 디렉토리 설정
WORKDIR /Gimbap_backend

# 소스 코드 복사
COPY ../requirements.txt .

# 의존성 설치
RUN pip install -r requirements.txt

COPY . /Gimbap_backend

# CMD 명령 실행
CMD ["python", "Gimbap_backend/manage.py", "runserver", "0.0.0.0:8080"]

# 포트 노출
EXPOSE 8080
