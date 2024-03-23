from django.test import TestCase
from find_machine.api_find_geo.models import Cargo, Truck, Location


class CargoModelTestCase(TestCase):

    def test_create_cargo(self):
        cargo = Cargo.objects.create(pickup_location='New York', delivery_location='Los Angeles', weight=500, description='Test cargo')
        self.assertEqual(cargo.pickup_location, 'New York')
        self.assertEqual(cargo.delivery_location, 'Los Angeles')
        self.assertEqual(cargo.weight, 500)
        self.assertEqual(cargo.description, 'Test cargo')


class TruckModelTestCase(TestCase):

    def test_create_truck(self):
        truck = Truck.objects.create(unique_number='1234A', current_location='New York', carrying_capacity=1000)
        self.assertEqual(truck.unique_number, '1234A')
        self.assertEqual(truck.current_location, 'New York')
        self.assertEqual(truck.carrying_capacity, 1000)


class LocationModelTestCase(TestCase):

    def test_create_location(self):
        location = Location.objects.create(city='New York', state='NY', zip_code='10001', latitude=40.7128, longitude=-74.0060)
        self.assertEqual(location.city, 'New York')
        self.assertEqual(location.state, 'NY')
        self.assertEqual(location.zip_code, '10001')
        self.assertEqual(location.latitude, 40.7128)
        self.assertEqual(location.longitude, -74.0060)