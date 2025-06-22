FROM python:3.8

# organize folders in the container, hence create working dir
WORKDIR /app

# copy reqs file into working dir created
COPY requirements.txt .

RUN pip install -r requirements.txt


# copy from local app folder into folder inside container
COPY ./app .

#entry point (it is within the container)
CMD ["python", "main.py"]