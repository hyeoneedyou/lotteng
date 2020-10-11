from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_on_sale_product_list_view, name="show_on_sale_product_list"),
]