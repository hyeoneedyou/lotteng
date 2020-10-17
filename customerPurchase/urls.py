from django.urls import path
from . import views

app_name="customerPurchase"
urlpatterns = [
    path('code/', views.purchasecode, name="purchasecode"),
    path('main/', views.purchase_main, name="purchase_main"),
    path('Lpay/', views.Lpay, name="Lpay"),
    path('card/', views.card, name="card"),
    path('phone/', views.phone, name="phone"),
    path('purchaselist/', views.purchaselist, name="purchaselist"),
]