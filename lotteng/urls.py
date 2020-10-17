from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('purchase/', include('customerPurchase.urls')),
    path('accounts/', include('allauth.urls')),
    path('onSale/', include('onSaleProduct.urls')),
    path('main/', include('main.urls')),
    path('shoppingCart/', include('shoppingCart.urls')),
]

