# Generated by Django 2.0.3 on 2018-04-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_event_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image10',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image3',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image4',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image5',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image6',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image7',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image8',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
        migrations.AddField(
            model_name='event',
            name='image9',
            field=models.FileField(blank=True, upload_to='Gallery/events'),
        ),
    ]