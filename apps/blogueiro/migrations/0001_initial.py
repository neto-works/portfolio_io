# Generated by Django 5.0.3 on 2024-03-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blogueiro",
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
                ("hastag", models.CharField(blank=True, max_length=50, null=True)),
                ("quant_post", models.IntegerField()),
            ],
        ),
    ]
