# Generated by Django 3.2.2 on 2021-05-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0005_page_shortdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='file',
            field=models.FileField(default=1, upload_to='PdfFile/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default=1, upload_to='PageImages/'),
            preserve_default=False,
        ),
    ]