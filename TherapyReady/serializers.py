from pyexpat import model
from rest_framework import serializers
from .models import Clinic, Therapist, User

class ClinicSerializer(serializers.ModelSerializer):
    # therapists = serializers.HyperlinkedRelatedField(
    #     view_name='therapist_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Clinic
        fields = ('id', 'image', 'name', 'street_number_and_name', 'city', 'state', 'phone_number', 'support_groups', )

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = ('id', 'clinic', 'name', 'bio', 'image', 'city', 'license', 'specialty', 'insurance_taken', 'price_range', 'sliding_scale', 'virtual', 'email', )