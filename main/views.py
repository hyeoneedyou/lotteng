from django.shortcuts import render
from onSaleProduct.views import get_on_sale_product_list, requestStrToInt
from shop.models import Shop

DEFAULT_PAGE_CNT = 10 # 한 페이지에 있는 상품의 기본 개수 
PAGE_NAV_LEFT = 5 # pageination nav bar의 왼쪽 넘버링 개수
PAGE_NAV_RIGHT = 5 # pageination nav bar의 오른쪽 넘버링 개수

# Create your views here.
def home(request):
    # request content
    page = requestStrToInt(request.GET.get('page')) # page 넘버
    page_cnt = requestStrToInt(request.GET.get('page_cnt', DEFAULT_PAGE_CNT)) # 한 페이지에 있는 상품의 수, defalt = 10
    company = request.GET.getlist('company')
    sort = request.GET.get('sort')
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    res = {}
    res.update(get_on_sale_product_list(page, company, sort, lat, lng, page_cnt)) 
    res['company'] = company
    res['page'] = page
    res['page_cnt'] = page_cnt
    if lat:
        res['lat'] = lat
    if lng:
        res['lng'] = lng
    if sort:
        res['sort'] = sort
    else:
        res['sort'] = "추천순"
    shopinfolist = Shop.objects.all() #지도에 표시될 각 매장의 정보 list
    context = {'shopInfoList' : shopinfolist}
    res.update(context) #res에 추가
    return render(request, 'home.html', res)

def show_team_profile(request):
    return render(request, 'team.html')
