# Generated by Django 3.2.6 on 2021-09-16 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500, verbose_name='body')),
                ('slug', models.SlugField(max_length=200, verbose_name='slug')),
                ('photo', models.ImageField(editable=False, upload_to='images', verbose_name='photo')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is_enabled')),
                ('likes', models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL, verbose_name='likes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
