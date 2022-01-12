from __future__ import absolute_import, unicode_literals
from celery import app
from apirate.coinMena.fetch_rate import fetch_rate
from celery import shared_task

@shared_task(name ='fetch_rate_task')
def fetch_rate_task():
    fetch_rate()
    print('done')