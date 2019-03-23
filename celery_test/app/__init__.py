from celery import Celery
from .config import Celery_config

app = Celery()
app.config_from_object(Celery_config)

