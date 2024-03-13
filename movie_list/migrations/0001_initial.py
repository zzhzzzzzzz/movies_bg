# Generated by Django 2.0 on 2024-02-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeekMovies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('releasedate', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('rate', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('kind', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=128)),
                ('time', models.CharField(max_length=128)),
                ('actor', models.TextField(null=True)),
            ],
            options={
                'db_table': 'week_movies',
            },
        ),
    ]
