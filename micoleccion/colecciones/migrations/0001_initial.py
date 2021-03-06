# Generated by Django 4.0.4 on 2022-05-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('numero', models.FloatField()),
                ('guionista', models.CharField(max_length=40)),
                ('dibujante', models.CharField(max_length=40)),
                ('editorial', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mangas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('autor', models.CharField(max_length=40)),
                ('editorial', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Novelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('editorial', models.CharField(max_length=40)),
            ],
        ),
    ]
