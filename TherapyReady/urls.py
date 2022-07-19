from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.homepage, name ='homepage'),
    path('clinics/', views.ClinicList.as_view(), name='clinic_list'),
    path('clinics/<int:pk>', views.ClinicDetail.as_view(), name='clinic_detail'),
    path('therapists/', views.TherapistList.as_view(), name='therapist_list'),
    path('therapists/<int:pk>', views.TherapistDetail.as_view(), name='therapist_detail'),
    path('clinics_protected/', views.ClinicListProtected.as_view(), name='clinic_list_protected'),
    path('therapists_protected/', views.TherapistListProtected.as_view(), name='therapist_list_protected')
]