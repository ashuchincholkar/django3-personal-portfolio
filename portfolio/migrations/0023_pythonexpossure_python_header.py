# Generated by Django 4.1.3 on 2022-12-21 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0022_pythonexpossure"),
    ]

    operations = [
        migrations.AddField(
            model_name="pythonexpossure",
            name="python_header",
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]