# NOTE: 自走プログラマー82:Docker公式のPythonを使う
# https://jisou-programmer.beproud.jp/%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%A7%8B%E6%88%90/82-Docker%E5%85%AC%E5%BC%8F%E3%81%AEPython%E3%82%92%E4%BD%BF%E3%81%86.html
# syntax=docker/dockerfile:1
FROM python:3.12.2
ENV PYTHONUNBUFFERED=1
RUN mkdir /djangoTaskApp
WORKDIR /djangoTaskApp
COPY requirements/requirements.txt /djangoTaskApp/
COPY requirements/requirements-dev.txt /djangoTaskApp/
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . /djangoTaskApp/
# dbshellを実行できるようにinstall
# NOTE: psqlのversionが15系でPostgreSQLが16系のためdbshell実行時には
# WARNINGが出るが、postgresql-client-16と指定してもパッケージがなく失敗するため、暫定的にpostgresql-clientをinstallしている
RUN apt-get update && apt-get install -y postgresql-client
