from celery import shared_task
from .models import Estate


@shared_task()
def plus_popular(estate_id):
    try:
        estate = Estate.objects.get(id=estate_id)
        estate.visits_counter()
        print('ready')
    except Estate.DoesNotExist:
        print('ERROR celery task: `plus_popular`')
