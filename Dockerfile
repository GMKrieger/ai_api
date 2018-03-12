FROM python:3.6.2

LABEL project.name="PFINAL"\
      image.content="API"\
      image.release-date="01-15-2018"\
      image.version="0.0.1"

COPY . /pf-api

WORKDIR /pf-api

RUN apt-get update

RUN apt-get install -y python3-dev

RUN pip3 install -r requirements.txt

ENV FLASK_CONFIG production

EXPOSE 5000

CMD ["invoke", "manager"]