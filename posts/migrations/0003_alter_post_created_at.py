# Generated by Django 3.2.8 on 2021-10-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211015_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime'),
        ),
    ]
