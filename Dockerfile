FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /api_service
WORKDIR /api_service
ADD . /api_service/
RUN pip install -r requirements.txt