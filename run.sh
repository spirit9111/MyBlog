sudo redis-server /etc/redis/redis.conf

celery -A celery_tasks.main worker -l info
