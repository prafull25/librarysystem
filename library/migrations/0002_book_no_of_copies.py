# Generated by Django 4.1.2 on 2022-10-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='no_of_copies',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]