# Generated by Django 4.1.3 on 2022-12-12 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0012_alter_project_to_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjSkills",
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
                ("skill", models.CharField(max_length=100)),
            ],
        ),
    ]
