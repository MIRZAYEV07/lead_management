# pull official base image
FROM python:3.11

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -r app && useradd -r -g app app

RUN mkdir -p /app/media /app/static \
    && chown -R app:app /app/    

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev && apt-get install -y python3-gdal \
  && apt-get install -y gettext-base gettext && apt-get install -y binutils libproj-dev

RUN apt-get install -y weasyprint

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# copy project
COPY . .
