# Generated by Django 3.0.5 on 2020-05-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200501_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
