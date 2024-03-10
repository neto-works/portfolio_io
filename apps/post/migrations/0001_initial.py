# Generated by Django 5.0.2 on 2024-03-10 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("blogueiro", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
                ("likes", models.IntegerField()),
                (
                    "imagem",
                    models.ImageField(blank=True, null=True, upload_to="images/posts/"),
                ),
                (
                    "blogueiro_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blogueiro.blogueiro",
                    ),
                ),
            ],
        ),
    ]
