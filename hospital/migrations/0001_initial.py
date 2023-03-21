# Generated by Django 4.1.7 on 2023-03-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('hospital_phone', models.CharField(max_length=14)),
                ('doctor_first_name', models.CharField(max_length=250)),
                ('doctor_lastname', models.CharField(max_length=250)),
                ('doctors_email', models.EmailField(max_length=254, unique=True)),
                ('doctors_phone', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]