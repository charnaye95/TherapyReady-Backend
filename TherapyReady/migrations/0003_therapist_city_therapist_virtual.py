# Generated by Django 4.0.6 on 2022-07-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TherapyReady', '0002_clinic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapist',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='therapist',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
    ]
