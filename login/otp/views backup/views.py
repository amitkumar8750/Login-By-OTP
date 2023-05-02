from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
from datetime import datetime
from validate_email_address import validate_email
import time






class LoginAPI(APIView):

	def post(self,request):

		try:
			data = request.data
			serializer = UserSerializer(data = data)
			# username = serializer.data['username']
			# user = login_details.objects.filter(username = username)
			
			
			if serializer.is_valid():

				# username = serializer.data['username']     # we can't use after is valid
				username = serializer.validated_data.get('username')  # It can be taken after is valid
				username_for_otp_verification=username
				user = login_details.objects.filter(username = username)

				if not user.exists():
				    serializer.save()
				    send_otp_via_email(serializer.data['username'])
				    return Response({
						'status' : 200,
						'message' : 'OTP is sent to your mail to confirm login',
						'data' : serializer.data,
						})		    
			
			username = serializer.data['username']
			username_for_otp_verification=username
			user = login_details.objects.filter(username = username)
			if user.exists():

				user=user.first()
				user.dt_updated=datetime.now()
				user.email_otp_used=False
				user.save()
				send_otp_via_email(serializer.data['username'])
				return Response({
						'status' : 200,
						'message' : 'OTP is sent to your mail to confirm login',
						'data' : serializer.data,
						})
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
			# u_serializer = UserSerializer(data = data)
			# username = u_serializer.data['username']

			if serializer.is_valid():

				# username = u_serializer.validated_data.get('username')
				# username = username_for_otp_verification
				email_otp = serializer.data['email_otp']
				
				user = login_details.objects.filter(email_otp = email_otp)
				if not user.exists():

					return Response({

				                        'status' : 400,
				                        'message' : 'something went wrong',
				                        'data' : "Invalid Email" })
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
			    		
			 

		except Exception as e:
			print(e)
