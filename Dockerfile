FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]
