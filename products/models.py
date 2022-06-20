from django.db import models
from users.models import myauth
class category(models.Model):
    category_name=models.CharField(max_length=70)
    def __str__(self):
        return self.category_name
class productsmodel(models.Model):
    name=models.CharField(max_length=256)
    image=models.ImageField(upload_to='products_image',blank=True)
    description=models.TextField(blank=True)
    short_description=models.CharField(max_length=64,blank=True)
    price=models.DecimalField(max_digits=8 ,decimal_places=2,default=0)
    quality=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class baskets(models.Model):
    product=models.ForeignKey(productsmodel,on_delete=models.CASCADE)
    user=models.ForeignKey(myauth,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.user.username} and {self.product.name}"
    def sum(self):
        return self.quantity*self.product.price