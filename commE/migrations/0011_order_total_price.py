# Generated by Django 4.2.4 on 2023-09-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commE', '0010_remove_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
