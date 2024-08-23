# Generated by Django 5.1 on 2024-08-23 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pessoas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                ("cep", models.CharField(max_length=100)),
                ("bairro", models.CharField(max_length=100)),
                ("logradouro", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="pessoa",
            name="endereco",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pessoas.endereco",
            ),
        ),
    ]
