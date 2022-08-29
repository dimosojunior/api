
from django.urls import path
from . import views

urlpatterns = [
    path('Welcome_Page/', views.Welcome_Page, name="Welcome_Page"),
    path('user_list_view/', views.user_list_view, name="user_list_view"),
    path('user_create_view/', views.user_create_view.as_view(), name="user_create_view"),
    
]