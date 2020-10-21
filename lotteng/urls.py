from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings 
from django.conf.urls.static import static
import re
from django.views.static import serve
from django.urls import re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('purchase/', include('customerPurchase.urls')),
    path('accounts/', include('allauth.urls')),
    path('onSale/', include('onSaleProduct.urls')),
    path('main/', include('main.urls')),
    path('shoppingCart/', include('shoppingCart.urls')),
    re_path(r'mdeditor/', include('mdeditor.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
