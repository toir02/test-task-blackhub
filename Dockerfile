FROM joyzoursky/python-chromedriver:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

CMD ["uvicorn", "main:app", "--reload"]
