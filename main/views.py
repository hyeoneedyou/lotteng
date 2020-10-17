from django.shortcuts import render
from onSaleProduct.views import get_on_sale_product_list
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_team_profile(request):
    return render(request, 'team.html')
    res = {}
    res.update(get_on_sale_product_list(1))
    return render(request, 'home.html', res)