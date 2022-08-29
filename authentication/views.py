from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.serializers import *
from DimosoApp.models import *
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@api_view(['GET'])
def Welcome_Page(request):
	my_urls={
		'Message':'Welcome To My Api Project',	
		'List_view':'/List_view/',
		'Detail_views/<str>':'/Detail_views',
		
	}

	return Response(my_urls,status=status.HTTP_200_OK)
# kwa ajili ya kucreate user  lkn ile form ya kujaza taarifa haionekani
# @api_view(['POST'])
# def user_create_view(request):
# 	serializer=UserCreationSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 		return Response(data=serializer.data,status=status.HTTP_201_CREATED)
	
# 	return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Nyingine kwa ajili ya kucreate user

class user_create_view(generics.GenericAPIView):
	serializer_class=UserCreationSerializer

	@swagger_auto_schema(operation_summary="User Registration Form")
	def post(self,request):
		data=request.data
		serializer=self.serializer_class(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data,status=status.HTTP_201_CREATED)

		return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_list_view(request):
	task = MyUser.objects.all()
	serializer = UserCreationSerializer(task, many=True)

	
	return Response(serializer.data)
