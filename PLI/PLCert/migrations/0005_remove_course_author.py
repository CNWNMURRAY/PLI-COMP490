# Generated by Django 2.0.2 on 2018-02-18 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PLCert', '0004_course_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
    ]
