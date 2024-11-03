FROM python:3.10
WORKDIR /taskmgmt
COPY requirements.txt /taskmgmt/
RUN pip install -r requirements.txt
COPY . /taskmgmt/