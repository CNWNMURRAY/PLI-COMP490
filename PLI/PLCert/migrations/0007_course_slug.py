# Generated by Django 2.0.2 on 2018-02-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PLCert', '0006_remove_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='None', max_length=200, unique=True),
        ),
    ]
