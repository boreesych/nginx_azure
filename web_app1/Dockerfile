FROM python:3.9-slim

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["flask", "run", "--port=8000", "--host=0.0.0.0"]