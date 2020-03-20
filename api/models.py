from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class UserBase(AbstractUser):
	username = models.CharField(blank=True, null=True, max_length=320)
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return "{}".format(self.email)


class User(models.Model):
	"""Class extending userbase 

	Helps adding more information on the user
	"""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='extra')
	first_name = models.CharField(max_length=30,blank=True)
	last_name = models.CharField(max_length=30,blank=True)




	