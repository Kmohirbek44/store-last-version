
from django.urls import path
from .views import registerfor,login,profilefor,logout

app_name='users'

urlpatterns = [

    path('auth/',login,name='login'),
    path('register/',registerfor,name='register'),
    path('profile/',profilefor,name='profile'),
    path('logout/',logout,name='logout')

]