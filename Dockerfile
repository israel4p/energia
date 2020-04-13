FROM alpine:3.11.2

RUN apk update --no-cache && \
    apk upgrade --no-cache && \
    apk add python3 --no-cache

ADD . /app
WORKDIR /app
RUN pip3 install --upgrade pip && \
    pip3 install -r requirementes.txt --upgrade

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
