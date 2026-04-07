FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN touch app/__init__.py \
    app/handlers/__init__.py \
    app/services/__init__.py

CMD ["python", "app/main.py"]