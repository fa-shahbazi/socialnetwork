# Generated by Django 3.2.6 on 2021-09-20 17:12

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=140)),
                ('gender', models.CharField(choices=[('female', 'f'), ('male', 'm'), ('others', 'other')], max_length=140)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='avatar')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='age')),
                ('phone_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True, verbose_name='phone number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profiles',
                'verbose_name_plural': 'profiles',
                'db_table': 'profiles',
            },
        ),
    ]
