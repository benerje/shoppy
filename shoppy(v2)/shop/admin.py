from django.contrib import admin

from .models import Product, Contact, Order, Customer, Ordercheckout

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Ordercheckout)
admin.site.register(Customer)
admin.site.register(Order)
