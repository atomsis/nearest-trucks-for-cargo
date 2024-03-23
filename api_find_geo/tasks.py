from celery import shared_task
from celery.utils.log import get_task_logger
import random
from .models import Truck, Location
from datetime import timedelta

logger = get_task_logger(__name__)

@shared_task
def update_truck_locations():
    trucks = Truck.objects.all()
    locations = Location.objects.all()
    for truck in trucks:
        truck.current_location = random.choice(locations)
        truck.save()
        logger.info(f"Updated location for truck {truck.id}")
