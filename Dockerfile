FROM python:3.12.5-bookworm
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT LOAN_APP=app.py flask run --host=0.0.0.0 --port=8080