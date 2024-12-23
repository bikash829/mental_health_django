# Generated by Django 5.1.2 on 2024-12-22 11:20

import apps.doctor_dashboard.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_alter_user_email_alter_user_marital_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('doc_title', models.IntegerField(blank=True, choices=[(1, 'Professor Dr.'), (2, 'Assistant Professor Dr.'), (3, 'Associate Professor Dr.'), (4, 'Distinguished Professor Dr.'), (5, 'Dr.')], default=0, null=True)),
                ('license_no', models.CharField(max_length=50)),
                ('license_attachment', models.FileField(upload_to=apps.doctor_dashboard.models.license_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
