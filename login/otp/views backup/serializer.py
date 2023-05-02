from rest_framework import serializers
from .models import login_details

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = login_details
		fields = ['username','email_otp_used']




	# dt_updated = serializers.DateTimeField()
	# email_otp_used = serializers.BooleanField()



		
class VerifyAccountSerializer(serializers.Serializer):

	username = serializers.EmailField()

	email_otp = serializers.CharField()
