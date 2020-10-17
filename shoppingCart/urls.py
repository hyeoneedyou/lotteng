from django.urls import path
from .views import *

app_name="shoppingCart"
urlpatterns = [
    path('<int:onSaleProduct_id>/like', like, name="onSaleProduct"),
    path('shoppingcart/', shoppingcart_list, name="shoppingcart_list"),
]