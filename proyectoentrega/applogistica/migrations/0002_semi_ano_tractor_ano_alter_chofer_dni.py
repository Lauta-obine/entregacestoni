# Generated by Django 5.1.4 on 2025-01-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applogistica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semi',
            name='ano',
            field=models.IntegerField(default='0000'),
        ),
        migrations.AddField(
            model_name='tractor',
            name='ano',
            field=models.IntegerField(default='0000'),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='dni',
            field=models.IntegerField(unique=True),
        ),
    ]