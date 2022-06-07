from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birthday = models.DateField()
	gender = models.CharField(
		max_length=6,
		choices=[('M', 'MALE'),  ('F', 'FEMALE')]
	)
	mobile = models.CharField(max_length=10)

	def __str__(self):
		return self.user.username