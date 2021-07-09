#import uuid

from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model 
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    Date_of_birth = models.DateField(default=timezone.now)
    Blood_group = models.CharField(max_length=25)
    Genotype = models.TextField()
    Vaccination_history = models.TextField(max_length=250)
    images = models.ImageField('images')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.First_name, self.Last_name) 
    
class Parent(models.Model):
    user = models.OneToOneField(
    get_user_model(), on_delete=models.CASCADE, related_name='parent')
    First_name = models.CharField(max_length=100, blank=True)
    Last_name = models.CharField(max_length=100, blank=True)
    Gender = models.TextField(max_length=25,blank=True)
    Email_address = models.EmailField(max_length=250, null=True)
    Phone_number = models.IntegerField(null=True)
    images = models.ImageField(upload_to= 'images', null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} {self.Last_name}"
    
    @receiver(post_save, sender=get_user_model())
    def create_or_update_user_parent(sender, instance, created, *args, **kwargs):
        if created:
            Parent.objects.create(user=instance)

    @receiver(post_save, sender=get_user_model())
    def save_user_parent(sender, instance, **kwargs):
        instance.parent.save()
    


class Hospital_Details(models.Model):
    hospital_Name = models.TextChoices('hospitalName', 'hosp1 hosp2')
    name = models.CharField(max_length=200)
    hospital = models.CharField(blank=True, choices=hospital_Name.choices, max_length=200)
    address = models.CharField("Address line 1", max_length=1024)
    vaccines = models.TextChoices('vaccines', 'Polio(IPV) Measles_mumps_rubella(MMR)')


class Hospital_Type(models.Model):
    HOSPITAL_TYPE_CHOICES =(
        ('private','private'),
        ('public', 'public'),
    ) 
    hospital_type = models.CharField(max_length=30, choices=HOSPITAL_TYPE_CHOICES, default='private')
    name = models.CharField(max_length=200)
    


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField
    end_time = models.TimeField
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.parent)















    


