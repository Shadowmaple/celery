# celery

## 启动

异步任务
```
celery -A xxx worker --loglevel=info
```

周期性任务
```
celery -A xxx worker -B
```

其中：

+ 参数 `-A` 指定了 Celery 实例的位置，Celery 会自动在该文件中寻找 Celery 对象实例，当然，我们也可以自己指定，使用 -A xxx；
+ 参数 `--loglevel` 指定了日志级别，默认为 `warning`，也可以使用 `-l info` 来表示
