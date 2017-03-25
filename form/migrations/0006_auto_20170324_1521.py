# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20170324_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='buyer_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=b'buyer'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=b'delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=b'order'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=b'role'),
        ),
        migrations.AlterField(
            model_name='sock',
            name='sock_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=b'sock'),
        ),
    ]
