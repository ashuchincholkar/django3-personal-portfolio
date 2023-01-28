# Generated by Django 4.1.3 on 2022-12-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_alter_project_roles"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjSummary",
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
                ("title", models.CharField(max_length=100)),
                ("summary", models.TextField(max_length=10000)),
            ],
        ),
    ]
