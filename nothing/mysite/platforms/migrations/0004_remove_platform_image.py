# Generated by Django 5.0.4 on 2024-04-18 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0003_platform_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='image',
        ),
    ]
