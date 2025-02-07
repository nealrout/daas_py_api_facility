from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Facility
from .serializers import FacilitySerializer, BulkFacilitySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    @action(detail=False, methods=['post'], url_path='bulk-upsert', url_name='bulk_upsert')
    def bulk_upsert(self, request):
        """Accepts a list of facilities and inserts or updates them."""
        serializer = BulkFacilitySerializer(data=request.data)
        if serializer.is_valid():
            facilities = serializer.save()
            return Response(
                {"message": "Facilities inserted/updated successfully", "count": len(facilities)},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)