# Generated by Django 4.0.6 on 2022-09-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_results_batch_results_batch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='specialization_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.specializations'),
            preserve_default=False,
        ),
    ]
