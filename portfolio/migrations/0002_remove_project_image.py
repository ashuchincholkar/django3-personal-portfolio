# Generated by Django 4.1.3 on 2022-12-06 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="image",),
    ]
