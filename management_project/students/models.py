from django.db import models

class STUDENT(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100, unique=True)
    student_age = models.IntegerField()


    def __str__(self):
        return str(self.student_name)


