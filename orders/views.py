from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.serializers import *
from drf_yasg.utils import swagger_auto_schema
from DimosoApp.models import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

# Create your views here.
@api_view(['GET'])

def Welcome_to_orders_Page(request):
	my_urls={
		'Message':'Welcome To Orders Page',	
		'List_view':'/List_view/',
		'Detail_views/<str>':'/Detail_views',
		
	}

	return Response(my_urls,status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
	serializer_class = OrderCreationSerializer
	queryset = Order.objects.all()
	permission_classes=[IsAuthenticated]
#kwa ajili  ya kudisplay orders
	@swagger_auto_schema(operation_summary="Get all orders")
	def get(self,request):
		orders = Order.objects.all()
		serializer=self.serializer_class(instance=orders,many=True)
		return Response(data=serializer.data,status=status.HTTP_200_OK)
#kwa ajili ya kuadd orders
	@swagger_auto_schema(operation_summary="Create a new order")
	def post(self,request):
		data=request.data
		serializer=self.serializer_class(data=data)
#in order to work import permissions
		user = request.user
		if serializer.is_valid():
			serializer.save(customer=user)
			return Response(data=serializer.data,status=status.HTTP_201_CREATED)

		return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#class kwa ajili ya kuview, kuupdate na kudelete order
class OrderDetailView(generics.GenericAPIView):
	serializer_class = OrderDetailSerializer
	#permission_classes=[IsAuthenticated]
	# queryset = Order.objects.all()
	# permission_classes=[IsAuthenticated]
#kwa ajili  ya kudisplay orders

#VIEW
	@swagger_auto_schema(operation_summary="Get a specific order")
	def get(self,request,order_id):
		order =get_object_or_404(Order,pk=order_id) 
		serializer=self.serializer_class(instance=order)
		return Response(data=serializer.data,status=status.HTTP_200_OK)

		#UPDATE
	@swagger_auto_schema(operation_summary="Update order")
	def put(self,request,order_id):
		data=request.data
		order =get_object_or_404(Order,pk=order_id)
		
		serializer=self.serializer_class(data=data,instance=order)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data,status=status.HTTP_200_OK)
		return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#DELETE
	@swagger_auto_schema(operation_summary="Delete order")
	def delete(self,request,order_id):
		order =get_object_or_404(Order,pk=order_id)
		order.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
		