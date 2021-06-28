import datetime
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class Child(models.Model):
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
    Date_of_birth = models.DateField
    Blood_group = models.CharField(max_length=25)
    Genotype = models.TextField()
    Vaccination_history = models.TextField(max_length=250)
    images = models.ImageField('images')


class Parent(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
    Email_address = models.EmailField(max_length=250)
    Password = models.TextField()
    Phone_number = models.IntegerField()
    images = models.ImageField('images')

class Hospital_Details(models.Model):
    hospital_Name = models.TextChoices('hospitalName', 'hosp1 hosp2')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_Name.choices, max_length=200)


class Hospital_Type(models.Model):
    hospital_type = models.TextChoices('hospitalType','public private')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_type.choices, max_length=100)


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField
    end_time = models.TimeField
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
       return self.parent



