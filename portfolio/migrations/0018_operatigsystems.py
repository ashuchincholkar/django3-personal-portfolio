# Generated by Django 4.1.3 on 2022-12-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0017_projtechstack_tech_summary"),
    ]

    operations = [
        migrations.CreateModel(
            name="OperatigSystems",
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
                ("os_system", models.TextField(max_length=500)),
            ],
        ),
    ]
