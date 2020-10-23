from django.http import request
from customer.models import Customer
from django.shortcuts import redirect, render, get_object_or_404
import random, json
from .models import CustomerPurchase
from onSaleProduct.models import OnSaleProduct
from shoppingCart.models import ShoppingCart

# Create your views here.
def purchasecode(request):
    code = random.randrange(0, 9999)
    code = (4 - len(str(code))) * "0" + str(code)
    return render(request, 'customerPurchase/purchasecode.html', {'code':code})

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

    msg = []
    for id, info in purchase_info.items():
        sale_product = get_object_or_404(OnSaleProduct, pk = id)
        stock = sale_product.stock
        purchase_cnt = int(info['cnt'])
        if stock < purchase_cnt:
            msg.append("[{}]{} {} 제품의 재고가 없습니다. 환불되었습니다.".format(info['shop'], info['company'], info['product']))
        else:
            sale_product.stock -= purchase_cnt
            msg.append("[{}]{} {} 제품이 구매되었습니다. 주문내역에서 인증번호를 확인하실 수 있습니다.".format(info['shop'], info['company'], info['product']))
        sale_product.save()

        cart_item = get_object_or_404(ShoppingCart, onSaleProduct = sale_product, customer__user = user)
        cart_item.delete()

    return render(request, 'customerPurchase/purchase_check.html', {'msg':msg})

def purchaselist(request):
    purchase_list = CustomerPurchase.objects.all()
    purchase_list = purchase_list.filter(customer__user = request.user)

    return render(request, "customerPurchase/purchaselist.html", {"purchase_list": purchase_list})
