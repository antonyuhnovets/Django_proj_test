# Generated by Django 3.2.8 on 2021-10-14 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_post_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
    ]
