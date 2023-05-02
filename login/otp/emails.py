from django.core.mail import send_mail
import random
from django.conf import settings
from .models import login_details
import time

def send_otp_via_email(username):

	subject = 'Your account verification email'
	email_otp = random.randint(1000 , 9999)
	message = f'Your otp is {email_otp}'
	email_from = settings.EMAIL_HOST
	send_mail(subject , message , email_from , [username])
	user_obj = login_details.objects.get(username = username)
	user_obj.email_otp = email_otp
	user_obj.save()


def OTP_Expire(username):
	user_obj = login_details.objects.get(username = username)
	time.sleep(30)
	if user_obj.email_otp_used==0:
		user_obj.email_otp = None
		user_obj.save()





# call another .py file in django:- https://stackoverflow.com/questions/546017/how-do-i-run-another-script-in-python-without-waiting-for-it-to-finish