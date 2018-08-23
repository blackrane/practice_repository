# Generated by Django 2.0.7 on 2018-08-23 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0017_merge_20180823_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='GCdislike_user_set', through='bbs.GalleryDisLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='Glike_user_set', through='bbs.GalleryLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gallerycomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbs_gallerycomments', to='bbs.Gallery', verbose_name='HoneyTip Comment'),
        ),
        migrations.AlterField(
            model_name='gallerydislike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_set', to='bbs.Gallery'),
        ),
        migrations.AlterField(
            model_name='gallerylike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='bbs.Gallery'),
        ),
    ]
