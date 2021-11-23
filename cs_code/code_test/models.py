from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import SmallIntegerField

from django.contrib.auth.models import User

from django.forms import ModelForm

class BillingPlan(models.Model):
    billing_plan_name = models.CharField(max_length=255)

    def __str__(self):
        return self.billing_plan_name

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    password_plain = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(editable=False, 
                                      auto_now_add=True, 
                                      auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      blank=True, 
                                      null=True)
    card_brand = models.CharField(max_length=255)
    card_last_four = models.CharField(max_length=4)
    trial_ends_at = models.DateTimeField()
    shop_domain = models.CharField(max_length=255)
    is_enabled = models.BooleanField(default=True)
    billing_plan = models.ForeignKey(BillingPlan, on_delete=PROTECT)
    trial_starts_at = models.DateTimeField()




    def __str__(self):
        return f'{self.name} of {self.shop_name}'

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name


class Style(models.Model):
    style_name = models.CharField(max_length=255)

    def __str__(self):
        return self.style_name


class ProductType(models.Model):
    product_type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_type_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    style = models.ForeignKey(Style, 
                              on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, 
                              on_delete=models.PROTECT)
    created_at = models.DateTimeField(editable=False, 
                                      auto_now_add=True, 
                                      auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      blank=True, 
                                      null=True)
    url = models.TextField(default='', blank=True)
    product_type = models.ForeignKey(ProductType, 
                                     on_delete=models.PROTECT)
    shipping_price = models.IntegerField()
    note = models.TextField(default='', blank=True)
    admin = models.ForeignKey(Admin, on_delete=PROTECT)

    def __str__(self):
        return f'{self.id} {self.product_name}'


class Inventory(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT)
    quantity = models.IntegerField()
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.FloatField()
    price_cents = models.IntegerField()
    sale_price_cents = models.IntegerField()
    cost_cents = models.IntegerField()
    sku = models.CharField(max_length=255)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    note = models.TextField()

    def __str__(self):
        return '{} {} {} {}'.format(self.product.product_name,
                                 self.color,
                                 self.size,
                                 self.quantity)

    class Meta:
        verbose_name_plural = "Inventories"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=PROTECT)
    inventory = models.ForeignKey(Inventory, on_delete=PROTECT)
    street_address = models.TextField()
    apartment = models.TextField()
    city = models.TextField()
    state = models.TextField()
    country_code = models.CharField(max_length=255)
    zip = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.TextField()
    name = models.CharField(max_length=255)
    order_status = models.CharField(max_length=255)
    payment_ref = models.TextField()
    transaction_id = models.CharField(max_length=255)
    payment_amt_cents = models.IntegerField()
    ship_charged_cents = models.IntegerField(null=True)
    ship_cost_cents = models.IntegerField(null=True)
    subtotal_cents = models.IntegerField()
    total_cents = models.IntegerField()
    shipper_name = models.TextField()
    payment_date = models.DateTimeField(blank=True, 
                                        null=True)
    shipped_date = models.DateTimeField(blank=True, 
                                        null=True)
    tracking_number = models.TextField()
    tax_total_cents = models.IntegerField()
    created_at = models.DateTimeField(editable=False, 
                                      auto_now_add=True, 
                                      auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      blank=True, 
                                      null=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.name,
                                    self.city,
                                    self.state,
                                    self.country_code,
                                    self.shipped_date)


class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name',
                  'description',
                  'style',
                  'brand',
                  'url',
                  'product_type',
                  'shipping_price',
                  'note',]
