from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacilityViewSet

router = DefaultRouter()
router.register(r'facility', FacilityViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    # path('facility/bulk_upsert/', FacilityViewSet.as_view({'post': 'bulk_upsert'}), name='bulk_upsert'),
]
