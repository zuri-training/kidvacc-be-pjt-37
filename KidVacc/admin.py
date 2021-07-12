from django.contrib import admin
from .models import Child, Parent, Hospital_Details,Hospital_Type, Appointment, Vaccine

# Register your models here.

admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Hospital_Details)
admin.site.register(Hospital_Type)
admin.site.register(Appointment)
admin.site.register(Vaccine)