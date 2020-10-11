from django.shortcuts import render
from .models import OnSaleProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta

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
def show_on_sale_product_list_view(request):
    # request content
    page = requestStrToInt(request.GET.get('page')) # page 넘버
    page_cnt = requestStrToInt(request.GET.get('page_cnt', DEFAULT_PAGE_CNT)) # 한 페이지에 있는 상품의 수, defalt = 10

    # query
    time_threshold = datetime.now()

    on_sale_products = OnSaleProduct.objects.all()
    on_sale_products = on_sale_products.filter(endDate__gt=time_threshold) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
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

'''
시장 철수, 할인 마감등이 되지 않은 할인 중인 상품 목록을 
다른 페이지에서 사용하기 위한 함수
'''
def get_on_sale_product_list(page, page_cnt):
    # query
    time_threshold = datetime.now()

    on_sale_products = OnSaleProduct.objects.all()
    on_sale_products = on_sale_products.filter(endDate__gt=time_threshold) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
    on_sale_products = on_sale_products[::-1] # 최근에 등록된 상품이 앞으로 오게 한다.

    # pagination
    paginator = Paginator(on_sale_products, page_cnt)
    on_sale_products_current_page = paginator.get_page(page)

    # pagination nav bar range
    start = max(int(page)-PAGE_NAV_LEFT, 1)
    end = min(int(page)+PAGE_NAV_RIGHT, paginator.num_pages)

    return {
        'on_sale_products_current_page': on_sale_products_current_page,
        'page': page, 
        'page_cnt': page_cnt, 
        'range' : [i for i in range(start, end+1)]
    }