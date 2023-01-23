# Generated by Django 4.1.5 on 2023-01-23 08:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("disasterApp", "0003_run"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("province", models.BigIntegerField()),
                ("district", models.CharField(max_length=50)),
                ("palika", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("ward", models.BigIntegerField()),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
                (
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="disasterApp.local",
                    ),
                ),
            ],
        ),
    ]
