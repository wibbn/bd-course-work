FROM python:3.9-alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

WORKDIR /src

RUN apk add build-base
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

RUN pip install pandas

COPY . /src

RUN pip install -e .

EXPOSE 8000:8000

CMD ["python", "manage.py"]