# Generated by Django 2.1 on 2018-09-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='day_slug',
            field=models.TextField(default='00-00-00'),
        ),
        migrations.AddField(
            model_name='review',
            name='images',
            field=models.FileField(default=None, upload_to='media/<django.db.models.fields.TextField>/'),
        ),
    ]
