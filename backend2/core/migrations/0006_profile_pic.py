# Generated by Django 2.2 on 2020-10-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201003_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default='user pics/pic.jpg', null=True, upload_to='user pics'),
        ),
    ]