# Generated by Django 2.2.4 on 2019-08-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190812_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_publish',
            field=models.DateTimeField(),
        ),
    ]
