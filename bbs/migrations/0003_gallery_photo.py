# Generated by Django 2.0.8 on 2018-09-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20180913_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/%Y/%m/%d', verbose_name='gallery photo'),
        ),
    ]
