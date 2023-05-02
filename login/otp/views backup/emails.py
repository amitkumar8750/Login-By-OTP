from django.core.mail import send_mail
import random
from django.conf import settings
from .models import login_details








def send_otp_via_email(username):

	subject = 'Your account verification email'
	email_otp = random.randint(1000 , 9999)
	message = f'Your otp is {email_otp}'
	email_from = settings.EMAIL_HOST
	send_mail(subject , message , email_from , [username])
	user_obj = login_details.objects.get(username = username)
	user_obj.email_otp = email_otp
	user_obj.save()
