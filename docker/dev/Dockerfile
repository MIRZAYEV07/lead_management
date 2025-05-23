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


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# copy project
COPY . .
