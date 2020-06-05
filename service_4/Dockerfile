FROM python:alpine3.11

RUN mkdir ./opt/service4

COPY . /opt/service4

WORKDIR /opt/service4

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]