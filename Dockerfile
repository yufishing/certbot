FROM python:slim

COPY server.py /usr/local/bin

RUN apt update; \
    apt install -y --no-install-recommends cron;\
    pip install certbot python-crontab; \
    rm -rf /var/lib/apt/lists/*

VOLUME ["/srv/www", "/etc/letsencrypt"]

EXPOSE 80

CMD [ "server.py", "80" ]


