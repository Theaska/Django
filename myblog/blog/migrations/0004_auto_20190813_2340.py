# Generated by Django 2.2.4 on 2019-08-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190813_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]