# Generated by Django 4.1.3 on 2022-12-09 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_alter_project_roles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="roles",
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
