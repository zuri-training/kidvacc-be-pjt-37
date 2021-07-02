<<<<<<< HEAD
from django.db import models
=======
import datetime
from django.db import models
from django.contrib.auth.models import User 
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
<<<<<<< HEAD
class child(models.Model):
=======
class Child(models.Model):
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
<<<<<<< HEAD
    Date_of_birth = models.DateField
=======
    #Date_of_birth = models.DateField()
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
    Blood_group = models.CharField(max_length=25)
    Genotype = models.TextField()
    Vaccination_history = models.TextField(max_length=250)
    images = models.ImageField('images')

<<<<<<< HEAD

class parent(models.Model):
=======
class Parent(models.Model):
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
    Email_address = models.EmailField(max_length=250)
    Password = models.TextField()
    Phone_number = models.IntegerField()
    images = models.ImageField('images')

<<<<<<< HEAD
class hospital_details(models.Model):
=======
class Hospital_Details(models.Model):
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
    hospital_Name = models.TextChoices('hospitalName', 'hosp1 hosp2')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_Name.choices, max_length=200)


<<<<<<< HEAD
class hospital_type(models.Model):
=======
class Hospital_Type(models.Model):
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
    hospital_type = models.TextChoices('hospitalType','public private')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_type.choices, max_length=100)


<<<<<<< HEAD
class appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField
    end_time = models.TimeField
    parent = models.ForeignKey(parent, on_delete=models.CASCADE)
=======
class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField
    end_time = models.TimeField
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
       return self.parent
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015



