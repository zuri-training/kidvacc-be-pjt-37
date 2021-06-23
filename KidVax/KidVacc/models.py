from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class child_details(models.Model):
    Fname = models.CharField(max_length=100)
    Mname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
    Date_of_birth = models.DateField
    Weight = models.CharField(max_length=30)
    Blood_group = models.CharField(max_length=25)
    Genotype = models.TextField()
    Vaccination_history = models.TextField(max_length=250)
    images = models.ImageField('images')


class parent_details(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Gender = models.TextField(max_length=25)
    Email_address = models.EmailField(max_length=250)
    Phone_number = models.IntegerField()
    images = models.ImageField('images')

class hospital_details(models.Model):
    hospital_Name = models.TextChoices('hospitalName', 'hosp1 hosp2')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_Name.choices, max_length=200)


class hospital_type(models.Model):
    hospital_type = models.TextChoices('hospitalType','public private')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_type.choices, max_length=100)

