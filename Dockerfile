FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    lsb-release \
    libssl1.1 \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://packages.couchbase.com/clients/c/repos/deb/couchbase.key | gpg --dearmor -o /usr/share/keyrings/couchbase-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/couchbase-archive-keyring.gpg] https://packages.couchbase.com/clients/c/repos/deb/ubuntu2004 focal focal/main" > /etc/apt/sources.list.d/couchbase.list && \
    apt-get update && apt-get install -y libcouchbase-dev libcouchbase3

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 10000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
