FROM nginx

WORKDIR /usr/src/app/nginx

COPY  isbn-conf.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf
#COPY  nginx.conf /etc/nginx/nginx.conf

ENV TZ=Pacific/Saipan
