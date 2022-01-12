import os 
from celery import Celery 
from celery.schedules import crontab
from django.apps import apps
from django.conf import settings
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apirate.settings') 
app = Celery('apirate')   
# Celery will apply all configuration keys with defined namespace  
app.config_from_object('django.conf:settings', namespace='CELERY')   
# Load tasks from all registered apps 
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



app.conf.beat_schedule = {
    #Scheduler Name
    'fetch-rate-every-hour': {
        'task': 'fetch_rate_task',  
        # Schedule      
        'schedule': 30.0,
    }
}