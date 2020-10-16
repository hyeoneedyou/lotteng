from django.shortcuts import render
from onSaleProduct.views import get_on_sale_product_list
# Create your views here.
def home(request):
    res = {}
    res.update(get_on_sale_product_list(1))
    return render(request, 'home.html', res)