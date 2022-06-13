FROM python:alpine
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt .
RUN apk update && apk add gcc python3-dev musl-dev postgresql-dev
RUN pip3 install -r requirements.txt
RUN apk del gcc python3-dev musl-dev
COPY . .
CMD python3 manage.py makemigrations --noinput && \
    while ! python3 manage.py migrate --noinput ; do sleep 1 ; done && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --noinput --email test@test.com --noinput ; \
    gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=PhotoGraphy.settings --workers=4 PhotoGraphy.wsgi