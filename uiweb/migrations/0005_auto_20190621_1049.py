# Generated by Django 2.2.1 on 2019-06-21 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiweb', '0004_comment_weibo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='weibo_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
