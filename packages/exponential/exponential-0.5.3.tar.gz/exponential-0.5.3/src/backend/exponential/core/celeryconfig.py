# celeryconfig.py
import os

exponential_redis_host = os.environ.get("exponential_REDIS_HOST")
exponential_redis_port = os.environ.get("exponential_REDIS_PORT")
if "BROKER_URL" in os.environ and "RESULT_BACKEND" in os.environ:
    # RabbitMQ
    broker_url = os.environ.get("BROKER_URL", "amqp://localhost")
    result_backend = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")
elif exponential_redis_host and exponential_redis_port:
    broker_url = f"redis://{exponential_redis_host}:{exponential_redis_port}/0"
    result_backend = f"redis://{exponential_redis_host}:{exponential_redis_port}/0"
# tasks should be json or pickle
accept_content = ["json", "pickle"]
