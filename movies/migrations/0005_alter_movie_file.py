# Generated by Django 5.1 on 2024-09-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_alter_movie_duration_alter_movie_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="file",
            field=models.FileField(default="", upload_to="movies/"),
        ),
    ]
