# Generated by Django 3.2.9 on 2021-11-18 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_topic_output'),
        ('analytics', '0003_auto_20211118_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='view',
            name='topic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
    ]