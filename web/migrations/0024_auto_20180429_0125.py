# Generated by Django 2.0.3 on 2018-04-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20180429_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='Profile_picture/'),
        ),
    ]
