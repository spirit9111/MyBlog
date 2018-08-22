#! /bin/bash

# 开启redis
sudo redis-server /etc/redis/redis.conf

# 开启celery
celery -A celery_tasks.main worker -l info &

# 开启uwsgi
# uwsgi --ini uwsgi.ini

# 开启/重启nginx
# sudo /etc/init.d/nginx restart