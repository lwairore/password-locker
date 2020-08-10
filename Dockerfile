FROM python:3.6

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

RUN mkdir /python_password_locker
WORKDIR /python_password_locker

COPY requirements.txt /python_password_locker/

RUN pip install -r requirements.txt

ADD . /python_password_locker/

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]