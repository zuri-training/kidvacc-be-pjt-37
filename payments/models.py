from django.db import models

# Create your models here.
class Payment(models.Model):
	reference = models.CharField(max_length=50)
	status = models.CharField(max_length=20)
	paid_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
	email = models.EmailField()
=======
	email = models.EmailField()
>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0
