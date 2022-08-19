from django.db import models

# Create your models here.


class Batches(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField()
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

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    type = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

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
    total_marks=models.IntegerField()
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