# Generated by Django 4.2.16 on 2024-10-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mytig", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProduitAvailable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("tigID", models.IntegerField(default="-1")),
            ],
            options={
                "ordering": ("tigID",),
            },
        ),
    ]
