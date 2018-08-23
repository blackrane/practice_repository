# Generated by Django 2.0.7 on 2018-08-23 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0013_auto_20180822_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbs_notices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
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