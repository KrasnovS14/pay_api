FROM python:3.10

WORKDIR /pay-api

COPY .requirements.txt /pay-api/requirements.txt

RUN pip3.10 install -r requirements.txt


COPY  ./pay_api


CMD ["uvicorn", "main:app", "--reload"]
