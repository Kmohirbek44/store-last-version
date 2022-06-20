from django.contrib import admin
from .models import productsmodel,baskets,category
# admin.site.register(productsmodel)
admin.site.register(baskets)
admin.site.register(category)
@admin.register(productsmodel)
class ProductsModel(admin.ModelAdmin):
    list_display = ('name','price','quality','category')
    fields = ('name','image',('price','quality'),'category')
class BasketforUseradmin(admin.TabularInline):
    model = baskets
    fields = ('product','quantity')
    readonly_fields = ('quantity',)
    extra = 0
