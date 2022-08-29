from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
from django.utils import timezone
#User = get_user_model()


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  #HII NI PATH KWA AJILI YA KUHIFADHI HIZO IMAGE      
def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"44.jpg"}'

#HII NI KWA AJILI YA KUPATA DEFAULT IMAGE KM MTU ASIPO INGIZA IMAGE ILI ISILETE ERRORS
def get_default_profile_image():
    return "media/44.jpg"

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='get_profile_image_filepath', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


        
class Post(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    
    title = RichTextUploadingField(blank=True, null=True)
    title_tag = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/")
    title_description = RichTextUploadingField(blank=True, null=True)


class Order(models.Model):
    SIZES=(
            ('SMALL','small'),
            ('MEDIUM','medium'),
            ('LARGE','large'),
            ('EXTRA_LARGE','extraLarge')
        )
    ORDER_STATUS=(
            ('PENDING','pending'),
            ('IN_TRANSIT','inTransit'),
            ('DELIVERED','delivered'),
            
        )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    size = models.CharField(max_length=20,choices=SIZES,default=[0][0])
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default=[0][0])
    quantity = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.username