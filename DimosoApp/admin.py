from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
	list_display = ["username","email"]
	
	search_fields=["username"]
class PostAdmin(admin.ModelAdmin):
	list_display = ["name", "post_date"]
	#prepopulated_fields={'slug':('name',)}
class OrderAdmin(admin.ModelAdmin):
	list_display = ["customer","size","status", "quantity", "created_at","updated_at"]
	list_filter=["size", "status","created_at", "updated_at"]
	search_fields=["customer"]

admin.site.register(Post, PostAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(MyUser, MyUserAdmin)