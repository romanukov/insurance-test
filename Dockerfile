FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

WORKDIR /app

COPY $PWD/dist .

RUN pip install --upgrade pip && apk add build-base && \
    pip install ./insurance-test-1.0.0.tar.gz

EXPOSE 8000
