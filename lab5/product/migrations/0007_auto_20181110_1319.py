# Generated by Django 2.1.2 on 2018-11-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20181107_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
