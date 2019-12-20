FROM tiangolo/uwsgi-nginx-flask
# RUN apk --update add bash nano

WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir  -U pip
RUN pip3 install -r requirements.txt