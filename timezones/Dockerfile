FROM ubuntu:16.04
MAINTAINER Omar Sarabia "elsarabia@hotmail.com";

RUN apt-get -yqq update
RUN apt-get install -yqq python python-dev python-pip

RUN mkdir /src

ADD . /src

WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

expose 5000

CMD python app.py
