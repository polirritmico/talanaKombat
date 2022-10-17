# syntax=docker/dockerfile:1
FROM python:3.10.8

WORKDIR /talana

COPY . /talana

COPY test/cases/fight_case1.json /talana/fight.json

CMD ["python", ".", "fight.json"]
