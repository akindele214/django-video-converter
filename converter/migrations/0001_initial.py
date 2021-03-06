# Generated by Django 3.0.8 on 2020-08-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConverterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('media', models.FileField(blank=True, upload_to='converter_folder/')),
                ('extension', models.CharField(choices=[('.mp4', 'Video Mp4'), ('.ts', 'Video TS'), ('.mp3', 'Audio Mp3'), ('.m4a', 'Audio M4a'), ('.flv', 'Flash Video'), ('.mkv', 'Video Matroska')], max_length=5)),
                ('output', models.FileField(blank=True, upload_to='output/')),
                ('converted', models.BooleanField(default=False)),
                ('processing', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
