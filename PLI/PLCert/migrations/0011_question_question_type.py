# Generated by Django 2.0.1 on 2018-04-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PLCert', '0010_auto_20180419_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
