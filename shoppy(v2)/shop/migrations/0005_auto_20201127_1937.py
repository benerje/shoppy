# Generated by Django 3.1.1 on 2020-11-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=111),
        ),
    ]