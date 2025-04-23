FROM python:3.11.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

RUN mkdir -p ./reporte

ENV DOCKER_ENV=1

RUN python src/main.py

EXPOSE 8081

CMD ["python3", "-m", "http.server", "8081", "--directory", "reporte"]