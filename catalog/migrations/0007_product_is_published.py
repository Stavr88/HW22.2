# Generated by Django 4.2.15 on 2024-09-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_alter_version_product_alter_version_status_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
    ]
