# Generated by Django 3.1.8 on 2022-01-23 21:36

from django.db import migrations

import djangocms_frontend.contrib.image.models
import djangocms_frontend.contrib.link.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("djangocms_frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carousel",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Carousel",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="CarouselSlide",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Carousel slide",
            },
            bases=(
                djangocms_frontend.contrib.link.models.GetLinkMixin,
                djangocms_frontend.contrib.image.models.ImageMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
    ]
