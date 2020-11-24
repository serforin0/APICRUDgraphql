FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

COPY requeriments.txt /code/

RUN python -m pip install -r requeriments.txt

COPY . /code/
