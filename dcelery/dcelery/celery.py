import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery('dcelery')
app.config_from_object("django.conf:settings", namespace='CELERY')
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.broker_connection_retry_on_startup = True

app.conf.task_routes = {
    'cworker.tasks.task1': {'queue': 'queue1'},
    'cworker.tasks.task2': {'queue': 'queue2'},
}

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }


app.autodiscover_tasks()

