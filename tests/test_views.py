from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Location, Truck, Cargo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from find_machine.api_find_geo.models import Cargo


class CargoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(city="New York", state="NY", zip_code="10001", latitude=40.7128,
                                                longitude=-74.0060)
        self.truck = Truck.objects.create(unique_number="1234A", current_location=self.location, capacity=500)
        self.cargo = Cargo.objects.create(pick_up_location=self.location, delivery_location=self.location, weight=200,
                                          description="Test cargo")

    def test_retrieve_cargo_with_nearest_trucks(self):
        response = self.client.get(f'/cargos/{self.cargo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('nearest_trucks', response.data)


class CargoViewSetTestCase(APITestCase):

    def test_list_cargo(self):
        mixer.cycle(5).blend(Cargo)
        url = reverse('cargo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_create_cargo(self):
        url = reverse('cargo-list')
        data = {'pickup_location': 'New York', 'delivery_location': 'Los Angeles', 'weight': 500, 'description': 'Test cargo'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cargo.objects.count(), 1)
        cargo = Cargo.objects.first()
        self.assertEqual(cargo.pickup_location, 'New York')
        self.assertEqual(cargo.delivery_location, 'Los Angeles')
        self.assertEqual(cargo.weight, 500)
        self.assertEqual(cargo.description, 'Test cargo')
