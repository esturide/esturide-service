FROM python:3.12.2
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./esturide_api /code/app
CMD ["uvicorn", "esturide_api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
