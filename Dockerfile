FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ANNUAL_RATE=0.005 \
    RATE_PER_VALUE=0.005 \
    BASE_VALUE=10000

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential libpq-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
