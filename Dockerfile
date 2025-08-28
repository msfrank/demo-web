FROM nginx:1.29-bookworm

# install python and flask system packages
RUN apt-get update
RUN apt-get -y install python3 python3-flask supervisor uwsgi uwsgi-plugin-python3
RUN apt-get -y install procps vim less

# copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-default.conf /etc/nginx/conf.d/default.conf

# copy uwsgi configuration
COPY uwsgi.ini /srv/uwsgi.ini

# copy supervisord configuration
COPY supervisord.conf /srv/supervisord.conf

# copy static content
COPY content /srv/content

# copy webapp
COPY webapp /srv/webapp

# run nginx in the foreground
CMD /usr/bin/supervisord -c /srv/supervisord.conf --nodaemon
