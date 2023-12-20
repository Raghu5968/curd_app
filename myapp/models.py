from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    class Meta:
        db_table='student_data'