# Generated by Django 2.2 on 2019-11-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygrades', '0017_auto_20191123_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.CharField(max_length=30, null=True),
        ),
    ]