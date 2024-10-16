# Generated by Django 5.1.2 on 2024-10-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity_proof',
            field=models.FileField(upload_to='media/identity_proof/<function user_directory_path at 0x000001CE9ABD5A80>'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='media/profile_photo/<function user_directory_path at 0x000001CE9ABD5A80>'),
        ),
    ]