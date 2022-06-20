from django.contrib import admin
from .models import myauth
from products.admin import BasketforUseradmin
# Register your models here.
# admin.site.register(myauth)
@admin.register(myauth)
class Myaut(admin.ModelAdmin):
    inlines = (BasketforUseradmin,)
