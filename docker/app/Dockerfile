FROM python:3.10

RUN groupadd -r app && useradd -r -g app app

RUN mkdir -p /app/media /app/static \
    && chown -R app:app /app/

RUN apt-get update && \
    apt-get install -y gettext-base gettext

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev && apt-get install -y python3-gdal \
  && apt-get install -y gettext-base gettext && apt-get install -y binutils libproj-dev

RUN apt-get install -y weasyprint
COPY ./requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY ./docker/app/gunicorn.conf.py /gunicorn.conf.py

COPY . /app/

WORKDIR /app

EXPOSE 8000

CMD gunicorn -c /gunicorn.conf.py --log-level=${DJANGO_LOGLEVEL}--max-requests=1000 --access-logfile - --error-logfile - --bind=0.0.0.0:8000 core.wsgi:application
