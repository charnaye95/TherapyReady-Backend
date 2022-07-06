from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('clinics/', views.ClinicList.as_view(), name='clinic_list'),
    path('clinics/<int:pk>', views.ClinicDetail.as_view(), name='clinic_detail'),
    path('therapists/', views.TherapistList.as_view(), name='therapist_list'),
    path('therapists/<int:pk>', views.TherapistDetail.as_view(), name='therapist_detail'),
]