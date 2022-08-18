# Generated by Django 4.1 on 2022-08-18 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_batches_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batches',
            name='end_year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1900)]),
        ),
    ]
