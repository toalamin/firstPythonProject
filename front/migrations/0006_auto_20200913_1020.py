# Generated by Django 3.1.1 on 2020-09-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20200913_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
