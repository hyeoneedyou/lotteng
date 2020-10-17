from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_on_sale_product_list, name="show_on_sale_product_list"),
    path('<int:id>', views.show_on_sale_product_detail, name="show_on_sale_product_detail"),
    path('get_company_filter', views.filter_company_filter, name="get_company_filter"),
    path('post_company_filter', views.filter_company_filter, name="post_company_filter"),
]