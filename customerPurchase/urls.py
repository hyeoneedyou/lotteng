from django.urls import path
from . import views

urlpatterns = [
    path('code/', views.purchasecode, name="purchasecode"),
    path('main/', views.purchase_main, name="purchase_main"),
    path('purchaselist/', views.purchaselist, name="purchaselist"),
    path('purchase_check/', views.purchase_check, name ="purchase_check"),
]