from . import app
from flask_mail import Message, Mail
from flask import Flask
import os

flask_app = Flask(__name__)
flask_app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = 'xxx <xxx@qq.com>'
))
mail = Mail(flask_app)


@app.task
def test():
    print('celery is running')

@app.task
def send_mail():
    #需要使用上下文
    with flask_app.app_context():
        msg = Message("Hello, world",
                recipients = ["xxx@qq.com"])
        msg.body = "email sender"
        mail.send(msg)
        return "<h1>Best wish to U!>_<?</h1>"


if __name__ == '__main__':
    flask.run()
