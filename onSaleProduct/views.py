from django.http import response
from django.shortcuts import get_object_or_404, render
from .models import OnSaleProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import HttpResponse
import json

DEFAULT_PAGE_CNT = 10 # 한 페이지에 있는 상품의 기본 개수 
PAGE_NAV_LEFT = 5 # pageination nav bar의 왼쪽 넘버링 개수
PAGE_NAV_RIGHT = 5 # pageination nav bar의 오른쪽 넘버링 개수

'''
request로 들어오는 문자열이 정당한 경우, int 로 변환
아닌 경우, default 값을 return 하는 함수 
'''
def requestStrToInt(str, defalut = 1):
    ret = defalut
    try:
        ret = int(str)
    except:
        ret = defalut
    return ret

'''
시장 철수, 할인 마감등이 되지 않은 할인 중인 상품 목록을 return하는 뷰
'''
def show_on_sale_product_list(request):
    # request content
    page = requestStrToInt(request.GET.get('page')) # page 넘버
    page_cnt = requestStrToInt(request.GET.get('page_cnt', DEFAULT_PAGE_CNT)) # 한 페이지에 있는 상품의 수, defalt = 10

    # query
    time_threshold = datetime.now()

    on_sale_products = OnSaleProduct.objects.all()
    on_sale_products = on_sale_products.filter(endDate__gt=time_threshold, stock__gt = 0) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
    
    company = request.GET.getlist('company')

    if company:
        query = Q()
        for i in company:
            query = query | Q(shop__company__name = i)
        on_sale_products = on_sale_products.filter(query)
        print(query)
    on_sale_products = on_sale_products[::-1] # 최근에 등록된 상품이 앞으로 오게 한다.


    # pagination
    paginator = Paginator(on_sale_products, page_cnt)
    on_sale_products_current_page = paginator.get_page(page)

    # pagination nav bar range
    start = max(int(page)-PAGE_NAV_LEFT, 1)
    end = min(int(page)+PAGE_NAV_RIGHT, paginator.num_pages)

    return render(request, 'show_on_sale_product_list.html',\
        {
            'on_sale_products_current_page': on_sale_products_current_page,
            'page': page, 
            'page_cnt': page_cnt, 
            'range' : [i for i in range(start, end+1)]
            
        })


def get_shop_dis(shop_lat, shop_lng, lat =  37.513859279255, lng = 127.095973):
    return (float(shop_lat) - float(lat))**2 + (float(shop_lng) - float(lng))**2

'''
시장 철수, 할인 마감등이 되지 않은 할인 중인 상품 목록을 
다른 페이지에서 사용하기 위한 함수
'''
def get_on_sale_product_list(page, company, sort, lat, lng, page_cnt = DEFAULT_PAGE_CNT):
    # query
    time_threshold = datetime.now()

    on_sale_products = OnSaleProduct.objects.all()
    
    on_sale_products = on_sale_products.filter(endDate__gt=time_threshold, stock__gt = 0) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
    
    if sort:
        if sort == "추천순":
            on_sale_products = on_sale_products.order_by('-updatedAt')
        elif sort == "저가순":
            on_sale_products = on_sale_products.order_by('price')
        elif sort == "고가순":
            on_sale_products = on_sale_products.order_by('-price')
    else:
        on_sale_products = on_sale_products.order_by('-updatedAt')
    
    if company:
        query = Q()
        for i in company:
            query = query | Q(shop__company__name = i)
        on_sale_products = on_sale_products.filter(query)

    if sort and sort == "거리순":
        on_sale_products = on_sale_products.all()
        on_sale_products = sorted(on_sale_products, key = lambda t : get_shop_dis(t.shop.latitude, t.shop.longitude, lat, lng))

    # pagination
    paginator = Paginator(on_sale_products, page_cnt)
    on_sale_products_current_page = paginator.get_page(page)

    # pagination nav bar range
    start = max(int(page)-PAGE_NAV_LEFT, 1)
    end = min(int(page)+PAGE_NAV_RIGHT, paginator.num_pages)

    return {
        'company' : company,
        'on_sale_products_current_page': on_sale_products_current_page,
        'page': page, 
        'page_cnt': page_cnt, 
        'range' : [i for i in range(start, end+1)]
    }

'''
시장 철수, 할인 마감등이 되지 않은 할인 중인 상품인 경우에만 상품 정보 뷰를 return
아닌 경우, is_not_on_sale_product.html을 404 status로 return
'''
def show_on_sale_product_detail(request, id):
    product = get_object_or_404(OnSaleProduct, pk = id)

    # 할인 시간이 지난 경우의 상품의 detail 페이지를 요구하는 경우
    if product.endDate < datetime.now() or product.stock <= 0:
        response = render(request, "is_not_on_sale_product.html")
        response.status_code = 404
        return response

    return render(request, 'show_on_sale_product_detail.html',\
        {
            'product': product,
        }
    )

'''
시장 철수, 할인 마감등이 되지 않은 할인 중인 상품을 
다른 페이지에서 사용하기 위한 함수
'''
def get_on_sale_product_detail(id):
    product = get_object_or_404(OnSaleProduct, pk = id)

    # 할인 시간이 지난 경우의 상품의 detail 페이지를 요구하는 경우
    if product.endDate < datetime.now():
        return None

    return {
        'product': product,
    }

def on_sale_product_search(request):
    # request content
    page = requestStrToInt(request.GET.get('page')) # page 넘버
    page_cnt = requestStrToInt(request.GET.get('page_cnt', DEFAULT_PAGE_CNT)) # 한 페이지에 있는 상품의 수, defalt = 10

    on_sale_product_list = OnSaleProduct.objects.all()
    q = request.GET.get('q', '')
    
    # pagination
    paginator = Paginator(on_sale_product_list, page_cnt)
    on_sale_products_current_page = paginator.get_page(page)

    # pagination nav bar range
    start = max(int(page)-PAGE_NAV_LEFT, 1)
    end = min(int(page)+PAGE_NAV_RIGHT, paginator.num_pages)

    
    if q:
        on_sale_product_list = on_sale_product_list.filter(Q(shop__name__icontains = q) | Q(product__name__icontains = q) | Q(shop__company__name__icontains = q))
    return render(request, 'search.html', {
        'on_sale_product_search' : on_sale_product_list,
        'q' : q,
    })


def get_company_filter():
    company_list = OnSaleProduct.objects.all()

    f = request.GET.getlist('f')

    if f:
        query = Q()
        for i in f:
            query = query | Q(Shop__company__icontains = i)
            company_list = company_list.filter(query)

    context = {'company_list':company_list}
    
    return HttpResponse(json.dumps(context), content_type="application/json")


def post_company_filter():
    company_list = OnSaleProduct.objects.all()

    f = request.POST.getlist('f')

    if f:
        query = Q()
        for i in f:
            query = query | Q(Shop__company__icontains = i)
            company_list = company_list.filter(query)

    context = {'company_list':company_list}
    
    return HttpResponse(json.dumps(context), content_type="application/json")

