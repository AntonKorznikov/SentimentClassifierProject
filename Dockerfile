FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ENV API_TOKEN=${API_TOKEN}
ENV MONGO_URI=${MONGO_URI}

CMD ["python", "src/app.py"]
