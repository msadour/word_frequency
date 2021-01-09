FROM python:3.8

MAINTAINER Mehdi Sadour

ENV PYTHONUNBUFFERED 1
RUN mkdir /word_frequency
WORKDIR /word_frequency
COPY requirements.txt /word_frequency/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /word_frequency/