# Generated by Django 3.1.1 on 2020-11-28 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_customer_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Ordercheckout',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.AddField(
            model_name='order',
            name='ordercheckout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.ordercheckout'),
        ),
    ]
