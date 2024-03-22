# Generated by Django 5.0.3 on 2024-03-22 17:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
