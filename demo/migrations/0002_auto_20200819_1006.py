# Generated by Django 3.0.8 on 2020-08-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demots',
            name='download_url',
            field=models.URLField(blank=True),
        ),
    ]
