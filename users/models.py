from django.contrib.auth.models import AbstractUser
from django.db import models

class myauth(AbstractUser):
    image=models.ImageField(upload_to='users_avatar',blank=True)

