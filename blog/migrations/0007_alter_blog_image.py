# Generated by Django 4.1.3 on 2022-12-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_delete_blogsimg_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="blog/images/"),
        ),
    ]