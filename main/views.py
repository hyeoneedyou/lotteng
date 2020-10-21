from django.shortcuts import render
from onSaleProduct.views import get_on_sale_product_list
from shop.models import Shop

# Create your views here.
def home(request):
    res = {}
    res.update(get_on_sale_product_list(1)) 
    shopinfolist = Shop.objects.all() #지도에 표시될 각 매장의 정보 list
    context = {'shopInfoList' : shopinfolist}
    res.update(context) #res에 추가
    return render(request, 'home.html', res)

def show_team_profile(request):
    return render(request, 'team.html')
