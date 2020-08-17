FROM python:3.8-alpine

WORKDIR /app

COPY $PWD/dist .

RUN pip install --upgrade pip && apk add build-base && \
    pip install ./insurance-test-1.0.0.tar.gz

EXPOSE 8000
