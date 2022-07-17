from django.db import models

# Create your models here.
class Clinic(models.Model):
    image = models.TextField(default='')
    name = models.CharField(max_length=100)
    street_number_and_name = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=10)
    support_groups = models.BooleanField()

    def __str__(self):
        return self.name

class Therapist(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='therapists')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.TextField()
    license = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    insurance_taken = models.TextField()
    price_range = models.CharField(max_length=100)
    sliding_scale = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    saved_therapists = models.TextField()

    def __str__(self):
        return self.name
