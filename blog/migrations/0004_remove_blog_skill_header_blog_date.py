# Generated by Django 4.1.3 on 2022-12-06 01:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_description"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="skill_header",),
        migrations.AddField(
            model_name="blog",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
