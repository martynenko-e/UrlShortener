FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
RUN mkdir /srv/logs
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/src/docker-entrypoint.sh"]