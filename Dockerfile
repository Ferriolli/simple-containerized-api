FROM python:3.10-slim-bullseye

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--reload"]