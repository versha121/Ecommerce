# Generated by Django 4.2.4 on 2023-09-05 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commE', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]