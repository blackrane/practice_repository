# Generated by Django 2.0.8 on 2018-08-21 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20180821_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumbitcoincomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbs_forumbitcoincomments', to='bbs.ForumBitCoin', verbose_name='HoneyTip Comment'),
        ),
    ]