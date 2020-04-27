FROM python:latest

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /opt/app

CMD ["uvicorn", "app:run", "--host", "localhost", "--port", "5000"]
