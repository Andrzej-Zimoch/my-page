# Generated by Django 3.1.3 on 2020-12-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0005_project_web_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='web_link',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
