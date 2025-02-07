from rest_framework import serializers
from .models import Facility

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class BulkFacilitySerializer(serializers.ListSerializer):
    """Handles bulk insert/update of facilities."""
    child = FacilitySerializer()

    def create(self, validated_data):
        """Bulk insert or update facilities"""
        facilities = []
        for facility_data in validated_data:
            fac_code = facility_data.get('fac_code')
            facility, created = Facility.objects.update_or_create(
                fac_code=fac_code,
                defaults=facility_data
            )
            facilities.append(facility)
        return facilities