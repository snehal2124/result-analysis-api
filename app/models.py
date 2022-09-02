from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Batches(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_year = models.IntegerField(
        validators=[MaxValueValidator(3000), MinValueValidator(1900)])
    end_year = models.IntegerField(
        validators=[MaxValueValidator(3000), MinValueValidator(1900)])
    code = models.CharField(max_length=100)
    specialization_id = models.ForeignKey(
        "Specializations", on_delete=models.CASCADE
    )


class Specializations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    no_of_years = models.IntegerField()
    no_of_semesters = models.IntegerField()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)


class Semesters(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    specialization_id = models.ForeignKey(
        "Specializations", on_delete=models.CASCADE
    )
    batch_id = models.ForeignKey(
        "Batches", on_delete=models.CASCADE
    )


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    semester_id = models.ForeignKey(
        "Semesters", on_delete=models.CASCADE
    )


class Results(models.Model):
    id = models.AutoField(primary_key=True)
    batch_id = models.ForeignKey(
        "Batches", on_delete=models.CASCADE
    )
    student_id = models.ForeignKey(
        "Students", on_delete=models.CASCADE
    )
    semester_id = models.ForeignKey(
        "Semesters", on_delete=models.CASCADE
    )
    marks_obtained = models.IntegerField()
