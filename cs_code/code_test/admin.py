from django.contrib import admin

from .models import Product, ProductType, Brand, Style, Inventory, Order, Admin, BillingPlan

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Style)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Admin)
admin.site.register(BillingPlan)
