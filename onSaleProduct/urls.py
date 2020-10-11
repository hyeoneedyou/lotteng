from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_on_sale_product_list, name="show_on_sale_product_list"),
    path('id:int', views.show_on_sale_product_detail, name="show_on_sale_product_list"),
]