# Generated by Django 2.2.3 on 2019-07-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190722_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]