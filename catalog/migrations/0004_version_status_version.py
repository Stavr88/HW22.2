# Generated by Django 4.2.15 on 2024-09-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="version",
            name="status_version",
            field=models.BooleanField(default=True),
        ),
    ]
