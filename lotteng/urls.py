from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
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
    re_path(r'mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)