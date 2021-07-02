from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Child, Parent, Hospital_Details,Hospital_Type, Appointment

# Register your models here.

admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Hospital_Details)
admin.site.register(Hospital_Type)
admin.site.register(Appointment)
>>>>>>> f16162068f7c18e34d16aca58c4bbe4ae7f26015
