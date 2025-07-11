FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "app/main.py"]

