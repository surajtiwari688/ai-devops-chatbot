FROM python:3.13-slim-trixie

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" \
    && python -m pip install --no-cache-dir --upgrade pip "msgpack>=1.2.1" \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY  app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
