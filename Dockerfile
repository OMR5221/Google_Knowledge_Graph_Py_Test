FROM python:3.7-alpine

WORKDIR /google_kg
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "kg_test.py"]
