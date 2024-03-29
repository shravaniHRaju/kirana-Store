# Generated by Django 5.0.2 on 2024-02-29 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_purchase"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                ("qty", models.FloatField()),
                ("price", models.FloatField()),
                ("total_amt", models.FloatField()),
                ("sale_date", models.DateTimeField(auto_now_add=True)),
                ("customer_name", models.CharField(blank=True, max_length=50)),
                ("customer_mobile", models.CharField(max_length=50)),
                ("customer_address", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
    ]
