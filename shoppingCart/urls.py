from django.urls import path
from .views import put_shopping_cart, shoppingcart_list, put_one_product

urlpatterns = [
    path('<int:onSaleProduct_id>', put_one_product, name="put_one_product"),
    path('put_shopping_cart', put_shopping_cart, name="put_shopping_cart"),
    path('', shoppingcart_list, name="shoppingcart_list"),
]