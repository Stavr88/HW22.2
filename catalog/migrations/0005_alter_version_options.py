# Generated by Django 4.2.15 on 2024-09-27 15:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_version_status_version"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="version",
            options={
                "ordering": ["product", "num_version"],
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
