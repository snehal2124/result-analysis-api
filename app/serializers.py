from rest_framework import serializers
from app.models import Batches, Specializations

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = (
            'id',
            'name',
            'start_year',
            'end_year',
            'code',
            'specialization_id'
        )


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = (
            'id',
            'name',
            'code',
            'no_of_years',
            'no_of_semesters'
        )
