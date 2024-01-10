from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

celery_app = Celery('core')

celery_app.config_from_object('core.settings.base', namespace='CELERY')

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

import os
from celery import Celery
from celery.beat import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

app = Celery('config')
app.config_from_object('django.conf:settings.base', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam': {
        'task': 'account.tasks.send_spam',
        'schedule': crontab(minute='*/1')
    }
}
