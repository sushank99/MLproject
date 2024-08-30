FROM python:3.11-slim

WORKDIR /application

COPY . /application

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
