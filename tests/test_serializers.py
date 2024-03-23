from find_machine.api_find_geo.serializers import CargoSerializer, TruckSerializer, LocationSerializer
from mixer.backend.django import mixer
from django.test import TestCase


class CargoSerializerTestCase(TestCase):

    def test_cargo_serializer(self):
        cargo_data = {'pickup_location': 'New York', 'delivery_location': 'Los Angeles', 'weight': 500, 'description': 'Test cargo'}
        serializer = CargoSerializer(data=cargo_data)
        self.assertTrue(serializer.is_valid())
        cargo = serializer.save()
        self.assertEqual(cargo.pickup_location, 'New York')
        self.assertEqual(cargo.delivery_location, 'Los Angeles')
        self.assertEqual(cargo.weight, 500)
        self.assertEqual(cargo.description, 'Test cargo')