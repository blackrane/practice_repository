# Generated by Django 2.0.8 on 2018-08-23 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bk_bbs', '0004_auto_20180822_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICORating',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_icoratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
        migrations.CreateModel(
            name='ICORatingBkComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_icoratingbkcomments', to=settings.AUTH_USER_MODEL, verbose_name='유저네임')),
            ],
        ),
        migrations.CreateModel(
            name='ICORatingComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_icoratingcomments', to=settings.AUTH_USER_MODEL, verbose_name='유저네임')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_icoratingcomments', to='bk_bbs.ICORating', verbose_name='ICORating')),
            ],
        ),
        migrations.CreateModel(
            name='ICORatingDisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislike_set', to='bk_bbs.ICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ICORatingLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='bk_bbs.ICORating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='icoratingbkcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bk_bbs_icoratingbkcomments', to='bk_bbs.ICORatingComment', verbose_name='ico comment'),
        ),
        migrations.AddField(
            model_name='icorating',
            name='dislike_user_set',
            field=models.ManyToManyField(blank=True, related_name='Iislike_user_set', through='bk_bbs.ICORatingDisLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='icorating',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='Iike_user_set', through='bk_bbs.ICORatingLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
