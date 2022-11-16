FROM python:3.8-slim

RUN pip install flask
RUN pip install gunicorn

ENV FLASK_APP=main
ENV PORT=$PORT

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT main:app