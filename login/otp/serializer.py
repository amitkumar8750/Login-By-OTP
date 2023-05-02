from rest_framework import serializers
from .models import login_details

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = login_details
		fields = ['username']




	
# fields = ['username','email_otp_used']

		
class VerifyAccountSerializer(serializers.Serializer):

	email_otp = serializers.CharField()
