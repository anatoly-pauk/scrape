# Generated by Django 2.2 on 2019-11-30 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygrades', '0021_auto_20191130_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
    ]