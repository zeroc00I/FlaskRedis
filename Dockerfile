FROM python:3.6-alpine 

RUN mkdir /home/flask/
RUN mkdir /home/flask/templates
COPY RedisQueue.py /home/flask/
COPY requirements.txt /home/flask/
COPY app.py /home/flask/
COPY templates/* /home/flask/templates/

WORKDIR /home/flask/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
