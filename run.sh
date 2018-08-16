sudo redis-server /etc/redis/redis.conf

celery -A celery_demo worker -l info