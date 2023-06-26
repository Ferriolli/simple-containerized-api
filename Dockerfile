FROM python:3.10-slim-bullseye

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip install -r requirements.txt

EXPOSE 8000:8000

CMD ["uvicorn", "app:app", "--reload"]