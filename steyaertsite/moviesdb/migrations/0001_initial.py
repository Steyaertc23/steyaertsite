# Generated by Django 4.2.1 on 2023-08-01 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=6)),
                ('disk', models.CharField(max_length=8)),
                ('movie_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesdb.movielist')),
            ],
        ),
    ]
