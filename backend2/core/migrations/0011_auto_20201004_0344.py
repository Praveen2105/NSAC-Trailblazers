# Generated by Django 2.2 on 2020-10-04 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_devicereports_oxygen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicereports',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
