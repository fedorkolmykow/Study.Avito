FROM python:3.7-alpine

RUN mkdir -p /app/
WORKDIR app

ADD app.py /app/
ADD requirements.txt /app/
ADD weatherUrl.conf /app/

EXPOSE 5001

RUN pip3 install -r requirements.txt
CMD [ "python3", "/app/app.py" ]
