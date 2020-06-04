FROM python:alpine3.11

RUN mkdir ./opt/servic3

COPY . /opt/service3

WORKDIR /opt/service3

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]