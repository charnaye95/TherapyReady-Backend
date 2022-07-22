from django.contrib import admin
from .models import Clinic, Therapist, User

# Register your models here.
admin.site.register(Clinic)
admin.site.register(Therapist)
admin.site.register(User)