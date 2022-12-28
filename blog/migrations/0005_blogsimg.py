# Generated by Django 4.1.3 on 2022-12-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_blog_skill_header_blog_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogsImg",
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
                ("image", models.ImageField(upload_to="blog/images/")),
            ],
        ),
    ]
