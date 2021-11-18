# Generated by Django 3.2.9 on 2021-11-18 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_topic_output'),
        ('analytics', '0002_remove_view_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='view',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='view',
            name='topic',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
    ]
