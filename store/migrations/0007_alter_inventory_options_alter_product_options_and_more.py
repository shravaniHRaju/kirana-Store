# Generated by Django 5.0.2 on 2024-02-29 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_inventory"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inventory",
            options={"verbose_name_plural": "6. Inventory"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "3. Product"},
        ),
        migrations.AlterModelOptions(
            name="purchase",
            options={"verbose_name_plural": "4. Purchase"},
        ),
        migrations.AlterModelOptions(
            name="sale",
            options={"verbose_name_plural": "5. Sale"},
        ),
        migrations.AlterModelOptions(
            name="unit",
            options={"verbose_name_plural": "2. Unit"},
        ),
        migrations.AlterModelOptions(
            name="vendor",
            options={"verbose_name_plural": "1. Vendors"},
        ),
    ]
