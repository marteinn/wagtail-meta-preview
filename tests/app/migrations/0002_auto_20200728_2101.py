# Generated by Django 3.0.8 on 2020-07-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterpage',
            name='another_description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='twitterpage',
            name='another_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='twitterpage',
            name='og_description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='twitterpage',
            name='og_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
