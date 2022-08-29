
from django.urls import path
from . import views

urlpatterns = [
    path('Welcome_to_orders_Page/', views.Welcome_to_orders_Page, name="Welcome_to_orders_Page"),
    #path('OrderListView/', views.OrderListView, name="OrderListView"),
    path('OrderCreateListView/', views.OrderCreateListView.as_view(), name="OrderCreateListView"),
    path('OrderDetailView/<int:order_id>/', views.OrderDetailView.as_view(), name="OrderDetailView"),
    path('OrderDetailView/<int:order_id>/', views.OrderDetailView.as_view(), name="OrderDetailView"),
    
]