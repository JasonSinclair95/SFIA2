FROM python:alpine3.11
RUN mkdir ./opt/service2
COPY . /opt/service2
WORKDIR /opt/service2
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]