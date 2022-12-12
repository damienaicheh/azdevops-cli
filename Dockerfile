FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app && chmod 770 /app
USER appuser

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install .

ENV PATH=/home/appuser/.local/bin:$PATH

ENTRYPOINT [ "azdevops" ]