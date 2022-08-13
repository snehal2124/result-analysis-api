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
