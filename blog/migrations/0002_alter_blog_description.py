# Generated by Django 4.1.3 on 2022-12-03 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(max_length=100),
        ),
    ]