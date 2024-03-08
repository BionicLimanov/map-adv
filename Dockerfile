FROM chetan1111/botasaurus:latest

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN python -m pip install  -r requirements.txt

RUN mkdir app
WORKDIR /app
COPY . /app
WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python3", "-m", "flask", "run"]

