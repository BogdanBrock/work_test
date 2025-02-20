FROM python:3.9

WORKDIR /app

RUN pip install uvicorn==0.34.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["uvicorn", "work_test.asgi:application", "--host", "0.0.0.0", "--port", "9000"]