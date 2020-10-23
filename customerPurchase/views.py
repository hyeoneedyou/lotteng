from django.http import request
from customer.models import Customer
from django.shortcuts import redirect, render, get_object_or_404
import random, json
from .models import CustomerPurchase
from onSaleProduct.models import OnSaleProduct
from shoppingCart.models import ShoppingCart
from shop.models import AuthNumber, Shop

# Create your views here.
def getPurchasecode(shop_name, company_name):
    code = random.randrange(0, 9999)

    auth_number_list = AuthNumber.objects.filter(shop__name = shop_name, shop__company__name = company_name)
    
    for i in range(10000):
        for num in auth_number_list:
            if(num.auth_number == code):
                code = random.randrange(0, 9999)
                break
        else:
            break
    else:
        print("인증번호 발급 실패")
        return "Fail"
    return code

def purchase_main(request):
    purchase_info = json.loads(request.POST.get('data'))
    data = request.POST.get('data')
    del_list = []
    for product in purchase_info:
        if purchase_info[product]['cnt'] == '0':
            del_list.append(product)
    for del_item in del_list:
        del purchase_info[del_item]
    return render(request, "customerPurchase/purchase_main.html", {"purchase_infos" : purchase_info, 'data': data})

def purchase_check(request):
    purchase_info = json.loads(request.POST.get('data'))
    using_tool = request.POST.get('using-tool')
    user = request.user
    customer = get_object_or_404(Customer, user = request.user)

    msg = []
    for id, info in purchase_info.items():
        sale_product = get_object_or_404(OnSaleProduct, pk = id)
        stock = sale_product.stock
        purchase_cnt = int(info['cnt'])
        if stock < purchase_cnt:
            msg.append("[{}]{} {} 제품의 재고가 없습니다. 환불되었습니다.".format(info['shop'], info['company'], info['product']))
        else:
            code = getPurchasecode(info['shop'], info['company'])
            if(code == "Fail"):
                msg.append("[{}]{} {} 제품 인증번호 발급에 실패하였습니다. 고객센터에 문의해주세요.".format(info['shop'], info['company'], info['product']))
            else:
                crt_shop = get_object_or_404(Shop, name = info['shop'], company__name = info['company'])
                crt_auth_number = AuthNumber(auth_number = code, shop = crt_shop)
                crt_auth_number.save()
                crt_customer_purchase = CustomerPurchase(onSaleProduct = sale_product, customer = customer, count = purchase_cnt, auth_number = crt_auth_number)
                crt_customer_purchase.save()
                sale_product.stock -= purchase_cnt
                msg.append("[{}]{} {} 제품이 구매되었습니다. 주문내역에서 인증번호를 확인하실 수 있습니다.".format(info['shop'], info['company'], info['product']))
        sale_product.save()

        try:
            cart_items = ShoppingCart.objects.filter(onSaleProduct = sale_product, customer__user = user)
            for cart_item in cart_items:
                cart_item.delete()
        except:
            pass

    return render(request, 'customerPurchase/purchase_check.html', {'msg':msg})

def purchaselist(request):
    purchase_list = CustomerPurchase.objects.all()
    purchase_list = purchase_list.filter(customer__user = request.user)

    return render(request, "customerPurchase/purchaselist.html", {"purchase_list": purchase_list})
