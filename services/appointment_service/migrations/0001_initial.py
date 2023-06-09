# Generated by Django 4.1.3 on 2023-04-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('meeting_date', models.DateField()),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('cancled', 'CANCLED'), ('approved', 'APPROVED')], default='pending', max_length=20)),
            ],
            options={
                'ordering': ['submit_time'],
                'permissions': [('cancel_appointment', 'Can cancel appointment')],
            },
        ),
    ]
