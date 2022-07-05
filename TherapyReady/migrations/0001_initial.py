# Generated by Django 4.0.5 on 2022-07-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street_number_and_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=10)),
                ('support_groups', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('saved_therapists', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.TextField()),
                ('license', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('insurance_taken', models.TextField()),
                ('price_range', models.CharField(max_length=100)),
                ('sliding_scale', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapists', to='TherapyReady.clinic')),
            ],
        ),
    ]