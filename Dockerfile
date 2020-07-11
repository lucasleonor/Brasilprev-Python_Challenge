FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV CONFIG_FILE /python_challenge/config.yml

VOLUME /python_challenge/

COPY ./requirements.txt /app

RUN pip install -U -r requirements.txt

COPY ./ /app