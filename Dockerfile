FROM ubuntu:24.04
FROM python:3.12.2
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY app /code/app

EXPOSE 80

ENTRYPOINT ["uvicorn", "app.main:root", "--host", "0.0.0.0", "--port", "80", "--reload"]
