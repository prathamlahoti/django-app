# Generated by Django 2.1.5 on 2019-02-04 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_id',
        ),
    ]
