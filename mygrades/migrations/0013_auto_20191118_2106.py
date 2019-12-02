# Generated by Django 2.2 on 2019-11-18 21:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygrades', '0012_studentgradebookreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgradebookreport',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student_gradebookreport', to='mygrades.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentgradebookreport',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
