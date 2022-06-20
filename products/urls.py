from django.urls import path
from .views import main,products,basket_add
app_name='products'
urlpatterns=[
    path('',main,name='main'),
    path('products/', products, name='product'),
    path('<int:category_id>/',products,name='category'),
    path('page/<int:page>/',products,name='page'),

    path('basked-add/<int:product_id>/',basket_add,name='basket_add')
]