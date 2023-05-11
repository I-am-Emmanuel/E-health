# Generated by Django 4.1.3 on 2023-05-11 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='medical_personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.medicalpersonnel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile.patientmodel'),
        ),
    ]
