from django.db import models

# Create your models here.

GENDER = [
    ("male", "MALE" ),
    ("female", "FEMALE")
]

class Student(models.Model):

    usn_number = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=80)
    # first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    gpa = models.FloatField(max_length=10, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True)

    def __str__(self):
        return f"Student: {self.name} {self.usn_number}"

# ds
class Notes(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=90)
    date_added = models.DateTimeField(auto_now_add=True)
    file = models.FileField( upload_to=None, max_length=100)

    def __str__(self):
        return self.title
