# Generated by Django 2.0.3 on 2018-04-27 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
