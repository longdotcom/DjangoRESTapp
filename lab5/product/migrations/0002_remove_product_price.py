# Generated by Django 2.1.2 on 2018-11-01 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
