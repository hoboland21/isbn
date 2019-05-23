FROM python:3.7.1-alpine3.8

WORKDIR /usr/src/app/django
COPY  requirements.txt /usr/src/app/django

RUN apk update  && \
   apk add --no-cache tzdata libc-dev musl-dev linux-headers pcre-dev python-dev mariadb-dev build-base mc &&\
   apk add gcc make 

RUN	pip install -r requirements.txt 


ENV TZ=Pacific/Saipan
