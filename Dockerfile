FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip \
    && && pip install --upgrade -r /requirements.txt

COPY . /app
ENV FLASK_APP=app.py
CMD ["flask", "run"]
