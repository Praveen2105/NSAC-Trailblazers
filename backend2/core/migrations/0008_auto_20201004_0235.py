# Generated by Django 2.2 on 2020-10-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201003_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicereports',
            name='ongoing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userreport',
            name='ongoing',
            field=models.BooleanField(default=False),
        ),
    ]