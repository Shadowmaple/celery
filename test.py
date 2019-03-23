from celery import Celery

app = Celery('test', backend='redis://localhost:6379/0', broker='redis://localhost:6379/1')

@app.task
def add():
    print('ok')

add()
