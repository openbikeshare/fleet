FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

CMD ["python", "main.py"]