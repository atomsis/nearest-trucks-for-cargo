from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import LocationViewSet,TruckViewSet,CargoViewSet

router = DefaultRouter()
router.register('locations',LocationViewSet)
router.register('trucks',TruckViewSet)
router.register('cargos',CargoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]