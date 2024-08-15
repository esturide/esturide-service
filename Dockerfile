FROM python:3.12.2
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY user_management_system /code/app
# CMD ["uvicorn", "user_management_system.app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
CMD ["uvicorn", "all_services.__init__:main", "--host", "0.0.0.0", "--port", "80", "--reload"]
