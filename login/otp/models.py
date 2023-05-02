from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid
from datetime import datetime





class login_details(models.Model):
	
	username = models.EmailField(unique=True)
	email_otp = models.CharField(max_length=6,null=True, blank=True)
	dt_created = models.DateTimeField(default=datetime.now())
	dt_updated = models.DateTimeField(default=datetime.now())
	email_otp_used = models.BooleanField(default=False,null=True, blank=True)

	class Meta:
		db_table="login_details"


