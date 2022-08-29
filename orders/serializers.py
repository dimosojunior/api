from rest_framework import serializers
from DimosoApp.models import *

class OrderCreationSerializer(serializers.ModelSerializer):
	size = serializers.CharField(max_length=20)
	status = serializers.HiddenField(default='PENDING')
	quantity = serializers.IntegerField()
    #created_at=serializers.DateTimeField(auto_now_add=True)
    #updated_at=serializers.DateTimeField(auto_now=True)

	class Meta:
		model= Order
		fields= ['id','size','status','quantity']
		#fields='__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
	size = serializers.CharField(max_length=20)
	status = serializers.CharField(default='PENDING')
	quantity = serializers.IntegerField()
	created_at=serializers.DateTimeField()
	updated_at=serializers.DateTimeField()

	class Meta:
		model= Order
		fields= ['size','status','quantity','created_at','updated_at']

