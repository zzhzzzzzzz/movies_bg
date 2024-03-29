# Generated by Django 2.0 on 2024-03-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0005_auto_20240310_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMovies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('C_title', models.CharField(max_length=128)),
                ('E_title', models.CharField(max_length=128)),
                ('releasedate', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('rate', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('kind', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('people', models.CharField(max_length=128)),
                ('actor', models.TextField(null=True)),
            ],
            options={
                'db_table': 'topmovies',
            },
        ),
    ]
