# Generated by Django 4.2.4 on 2023-09-11 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commE', '0008_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='lname',
        ),
    ]
