# Generated by Django 3.1.3 on 2020-11-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='git_link',
            field=models.CharField(default='', max_length=250),
        ),
    ]
