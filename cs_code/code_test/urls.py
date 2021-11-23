from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('products/', TemplateView.as_view(template_name='product_list.html'), name='product_list'),
    path('products/', views.products, name='products_list'),
    path('product/<int:product_id>', views.product, name='product_detail'),
    path('product/<int:product_id>/edit', views.productedit, name='product_edit'),
    path('inventory/', views.inventory, name='inventory'),
]