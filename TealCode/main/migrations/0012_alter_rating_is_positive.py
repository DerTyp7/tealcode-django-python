# Generated by Django 3.2.9 on 2021-11-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='is_positive',
            field=models.IntegerField(),
        ),
    ]
