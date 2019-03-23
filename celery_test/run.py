from app import tasks, app

tasks.send_mail.apply_async()
#task.send_mail()
tasks.test.apply_async()

print('OK')
