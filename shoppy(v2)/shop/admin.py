from django.contrib import admin

from .models import Product, Contact, Ordercheckout, Order

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Ordercheckout)
admin.site.register(Order)
