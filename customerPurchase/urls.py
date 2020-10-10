from django.urls import path
from . import views

app_name="customerPurchase"
urlpatterns = [
    path('', views.purchasecode, name="purchasecode"),
]