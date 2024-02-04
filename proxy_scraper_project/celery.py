from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery.schedules import crontab
from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proxy_scraper_project.settings')
app = Celery('proxy_scraper_project')
app.conf.enable_utc =False
app.conf.update(timezone ='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind= True)
def debug_task(self):
    print(f"request: {self.request!r}")


# Schedule Celery task
app.conf.beat_schedule = {
    'scrape-every-day': {
        'task': 'proxy_scraper.tasks.scrape_proxy_list',
        'schedule': crontab(minute=20, hour=18),  # Run the task every day at midNight
    },
}