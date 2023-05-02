from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
from datetime import datetime
from validate_email_address import validate_email
import time
# import validate_email



class LoginAPI(APIView):

	def post(self,request):

		try:
			data = request.data
			serializer = UserSerializer(data = data)			
			
			if serializer.is_valid():

				# username = serializer.data['username']     # we can't use after is valid
				username = serializer.validated_data.get('username')  # It can be taken after is valid
				user = login_details.objects.filter(username = username)

				if not user.exists():
				    serializer.save()
				    send_otp_via_email(serializer.data['username'])
				    LoginAPI.post.exp_time_count=time.time()
				    return Response({
						'status' : 200,
						'message' : 'OTP is sent to your mail to confirm login',
						'data' : serializer.data
                                                 
						})		                  
			
			username = serializer.data['username']
			user = login_details.objects.filter(username = username)
			if user.exists():

				user=user.first()
				user.dt_updated=datetime.now()
				user.email_otp_used=False
				user.save()
				send_otp_via_email(serializer.data['username'])
				LoginAPI.post.exp_time_count=time.time()
				return Response({
						'status' : 200,
						'message' : 'OTP is sent to your mail to confirm login',
						'data' : serializer.data })	
			elif not user.exists() and validate_email('username')==False:

				return Response({

				'status' : 400,
				'message' : 'something went wrong',
				'data' : serializer.errors })		
			

		except Exception as e:
			print(e)

				    	
class VerifyOTP(APIView):

	def post(self, request):

		try:

			data = request.data
			serializer = VerifyAccountSerializer(data = data)
			LoginAPI.post(self,request)
			# email_otp = serializer.data['email_otp']
			# user_obj = login_details.objects.get(email_otp = email_otp)

			if LoginAPI.post.exp_time_count+100>=time.time():

				if serializer.is_valid():

					email_otp = serializer.data['email_otp']
					user = login_details.objects.filter(email_otp = email_otp)
					if user[0].email_otp !=email_otp:

						return Response({

					                        'status' : 400,
					                        'message' : 'something went wrong',
					                        'data' : "Wrong OTP" })
					user = user.first()
					user.email_otp_used = True
					user.save()

					return Response({

				    	'status' : 200,
				    	'message' : 'account verified',
				    	'data' : {} })
			else:

				return Response({ 'status' : 400,
					               'message' : 'something went wrong',
					               'data' : "OTP is Expired"})
						    		
		except Exception as e:
			print(e)



