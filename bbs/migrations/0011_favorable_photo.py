# Generated by Django 2.0.7 on 2018-08-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0010_auto_20180822_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorable',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]