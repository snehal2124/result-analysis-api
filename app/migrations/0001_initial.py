# Generated by Django 4.0.5 on 2022-08-19 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.batches')),
            ],
        ),
        migrations.CreateModel(
            name='Specializations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('no_of_years', models.IntegerField()),
                ('no_of_semesters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('total_marks', models.IntegerField()),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semesters')),
            ],
        ),
        migrations.AddField(
            model_name='semesters',
            name='specialization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specializations'),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marks_obtained', models.IntegerField()),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.batches')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semesters')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.students')),
            ],
        ),
        migrations.AddField(
            model_name='batches',
            name='specialization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specializations'),
        ),
    ]
