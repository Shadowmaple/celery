from datetime import timedelta
from celery.schedules import crontab

class Celery_config(object):
    # Broker and Backend
    BROKER_URL = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Timezone
    CELERY_TIMEZONE='Asia/Shanghai'

    CELERY_IMPORTS = (
        'app.tasks'
    )

    # schedules
    CELERYBEAT_SCHEDULE = {
        'add-every-30-seconds': {
             'task': 'app.tasks.send_mail',
             'schedule': timedelta(seconds=30),
    #         'args': ()
        },
         'multiply-at-some-time': {
            'task': 'celery_app.task.lession',
            'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
    #       'args': ()                               # 任务函数参数
        }
    }
