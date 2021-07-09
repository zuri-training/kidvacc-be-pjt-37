from django.db import models

# Create your models here.
class Payment(models.Model):
	reference = models.CharField(max_length=50)
	status = models.CharField(max_length=20)
	paid_at = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
