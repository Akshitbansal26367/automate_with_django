import os
import multiprocessing
from celery import Celery

try:
    multiprocessing.set_start_method("spawn")
except RuntimeError:
    pass
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awd_main.settings')

# Sets up the new celery application for our Django project 'awd_main'
app = Celery('awd_main')

# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 