# Generated by Django 3.2.6 on 2021-09-16 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210916_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.DeleteModel(
            name='CommentVote',
        ),
    ]