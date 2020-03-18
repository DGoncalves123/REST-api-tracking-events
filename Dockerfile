FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
