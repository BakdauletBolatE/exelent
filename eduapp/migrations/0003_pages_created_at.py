# Generated by Django 3.2.2 on 2021-05-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0002_pages_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]