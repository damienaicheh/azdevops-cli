FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install .

ENV PATH=/home/appuser/.local/bin:$PATH
ENV GIT_PYTHON_REFRESH=quiet

ENTRYPOINT [ "azdevops" ]