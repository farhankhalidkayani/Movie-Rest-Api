# Generated by Django 5.1.2 on 2024-10-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movie_moviedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='Comedy', max_length=200),
        ),
    ]
