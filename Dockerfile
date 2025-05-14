
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    libssl1.1 \
    libcouchbase3 \
    libcouchbase-dev \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

# Set environment variable
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]