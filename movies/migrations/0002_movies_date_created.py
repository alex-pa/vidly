# Generated by Django 2.1 on 2020-09-15 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
