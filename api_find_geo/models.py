from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from geopy.distance import geodesic


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.CharField()

    def __str__(self):
        return f'{self.city}, {self.state}, {self.zip_code}'


class Truck(models.Model):
    uniq_number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='cars_location')
    capacity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return self.uniq_number


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pick_up_cargos')
    delivery_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='delivery_cargos')
    weight = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def near_truck_for_cargo(self):
        pick_up_coords = (self.pick_up_location.latitude, self.pick_up_location.longitude)
        trucks = Truck.objects.all()
        nearest_trucks = []

        for truck in trucks:
            truck_location = (truck.current_location.latitude, truck.current_location.longitude)
            distance = geodesic(pick_up_coords, truck_location).miles
            if distance <= 450:
                nearest_trucks.append({'truck': truck, 'distance': distance})

        return nearest_trucks

    def __str__(self):
        return self.description
