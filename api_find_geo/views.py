from django.shortcuts import render
from .models import Location, Truck, Cargo
from .serializers import LocationSerializer, TruckSerializer, CargoSerializer
from rest_framework import viewsets
from geopy.distance import geodesic
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def get_queryset(self):
        queryset = Cargo.objects.all()
        pick_up_location = self.request.query_params.get('pick_up_location', None)
        delivery_location = self.request.query_params.get('delivery_location', None)
        if pick_up_location and delivery_location:
            queryset = queryset.filter(pick_up_location__zip_code=pick_up_location,
                                       delivery_location__zip_code=delivery_location)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for cargo in data:
            cargo['nearest_trucks'] = self.get_nearest_trucks(cargo['pick_up_location'], cargo['delivery_location'])
        return Response(data)

    def get_nearest_trucks(self, pick_up_location, delivery_location):
        pick_up_location_obj = Location.objects.get(zip_code=pick_up_location)
        delivery_location_obj = Location.objects.get(zip_code=delivery_location)
        distance = geodesic((pick_up_location_obj.latitude, pick_up_location_obj.longitude),
                            (delivery_location_obj.latitude, delivery_location_obj.longitude)).miles
        trucks = Truck.objects.filter(current_location__in=[pick_up_location_obj, delivery_location_obj])
        nearest_trucks = []
        for truck in trucks:
            nearest_trucks.append({
                'number': truck.number,
                'distance_to_pick_up': geodesic((truck.current_location.latitude, truck.current_location.longitude),
                                                (pick_up_location_obj.latitude, pick_up_location_obj.longitude)).miles,
                'distance_to_delivery': geodesic((truck.current_location.latitude, truck.current_location.longitude),
                                                 (
                                                     delivery_location_obj.latitude,
                                                     delivery_location_obj.longitude)).miles
            })
        return nearest_trucks

    def get_truck_locations(self):
        truck_locations = Cargo.objects.values_list('pickup_location__latitude', 'pickup_location__longitude')
        return truck_locations

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['nearest_trucks'] = self.get_nearest_trucks(instance.pick_up_location.zip_code,
                                                         instance.delivery_location.zip_code)
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['nearest_trucks'] = self.get_nearest_trucks(instance.pick_up_location.zip_code,
                                                         instance.delivery_location.zip_code)
        return Response(data)
