# Generated by Django 2.0.8 on 2018-08-28 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bk_bbs', '0005_auto_20180823_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BKICORating',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_bkicoratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
        migrations.CreateModel(
            name='BKICORatingDisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_set', to='bk_bbs.BKICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BKICORatingLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='bk_bbs.BKICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ColumBKICORating',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_columbkicoratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
        migrations.CreateModel(
            name='ColumBKICORatingDisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_set', to='bk_bbs.ColumBKICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ColumBKICORatingLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='bk_bbs.ColumBKICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='columbkicorating',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='colbkIcodislike_user_set', through='bk_bbs.ColumBKICORatingDisLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='columbkicorating',
            name='ico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_columbkicoratings', to='bk_bbs.ICORating'),
        ),
        migrations.AddField(
            model_name='columbkicorating',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='colbkIcolike_user_set', through='bk_bbs.ColumBKICORatingLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bkicorating',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='bkIcodislike_user_set', through='bk_bbs.BKICORatingDisLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bkicorating',
            name='ico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_bkicoratings', to='bk_bbs.ICORating'),
        ),
        migrations.AddField(
            model_name='bkicorating',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='bkIcolike_user_set', through='bk_bbs.BKICORatingLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
