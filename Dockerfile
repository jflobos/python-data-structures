FROM python:3.7.2-alpine
RUN apk add --no-cache bash
ADD . /code/
WORKDIR /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

