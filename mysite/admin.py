from django.contrib import admin
from .models import Customers
from .models import cart,products,productcategory

# Register your models here.

class CustomView(admin.ModelAdmin):
    list_display=['customerno','name','lastname']

admin.site.register(Customers, CustomView)
admin.site.register(cart)
admin.site.register(products)
admin.site.register(productcategory)
#admin.site.register(contact)
#admin.site.register(productcategory)