# Generated by Django 4.1.3 on 2022-12-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0013_projskills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projskills",
            name="skill",
            field=models.TextField(max_length=500),
        ),
    ]
