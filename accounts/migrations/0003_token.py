# -*- coding: utf-8 -*-
# Generated by Django 2.1 on 2018-09-24 01:59
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0002_auto_20180923_1848")]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        )
    ]
