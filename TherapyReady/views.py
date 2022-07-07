from django.shortcuts import render
from django.http import JsonResponse
from .models import Clinic, Therapist
from rest_framework import generics
from .serializers import ClinicSerializer, TherapistSerializer

# Create your views here.
class ClinicList(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class TherapistList(generics.ListCreateAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

class TherapistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

def homepage(request):
    return render(request, 'TherapyReady/homepage.html')
