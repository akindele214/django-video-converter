# Generated by Django 3.0.8 on 2020-08-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20200821_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convertermodel',
            name='converted',
        ),
        migrations.RemoveField(
            model_name='convertermodel',
            name='processing',
        ),
        migrations.AlterField(
            model_name='convertermodel',
            name='output_extension',
            field=models.CharField(choices=[('', 'Select Extension'), ('.mp4', 'Video Mp4'), ('.ts', 'Video TS'), ('.mp3', 'Audio Mp3'), ('.m4a', 'Audio M4a'), ('.flv', 'Flash Video'), ('.mkv', 'Video Matroska')], max_length=5),
        ),
        migrations.AlterField(
            model_name='convertermodel',
            name='uploaded_extension',
            field=models.CharField(choices=[('', 'Select Extension'), ('.mp4', 'Video Mp4'), ('.ts', 'Video TS'), ('.mp3', 'Audio Mp3'), ('.m4a', 'Audio M4a'), ('.flv', 'Flash Video'), ('.mkv', 'Video Matroska')], max_length=5),
        ),
    ]
