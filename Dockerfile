FROM python:3.8.16-alpine
ENV PYTHONBUFFERED 1

RUN apk update && apk upgrade
RUN apk add pkgconfig git gcc gpgme-dev libc-dev

COPY ./. /application/.

WORKDIR /application

RUN pip3 install --upgrade pip
RUN pip3 install setuptools==30.1.0
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD exec daphne -b 0.0.0.0 -p 5000 core.asgi:application --websocket_connect_timeout 1800