import json
from django.http import request
from django.http.response import HttpResponse
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from onSaleProduct.models import OnSaleProduct
from shop.models import Shop
from .models import ShoppingCart
from django.shortcuts import get_object_or_404, render


@login_required
def pop_one_product(request):
    shoppingCartId = request.POST.get('shoppin_cart_product_id', None)
    
    shoppingCartProduct = get_object_or_404(ShoppingCart, pk = shoppingCartId)
    shoppingCartProductName = shoppingCartProduct.onSaleProduct.product.name

    shoppingCartProduct.delete()

    context = {
        "productName":shoppingCartProductName,
        "isPop" : True,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
def put_one_product(request):
    # ajax 통신을 통해서 template에서 POST방식으로 전달
    onSaleProduct_id = request.POST.get('onSaleProduct_id', None)
    cnt = 1

    shoppingCartList = ShoppingCart.objects.all()
    shoppingCartList = shoppingCartList.filter(customer__user=request.user)

    isPutCart = True

    for cartProduct in shoppingCartList:
        if int(cartProduct.onSaleProduct.id) == int(onSaleProduct_id):
            isPutCart = False
            break
    else:
        isPutCart = True
        tmp = ShoppingCart(
            onSaleProduct = OnSaleProduct.objects.filter(pk = onSaleProduct_id).first(), 
            customer = Customer.objects.filter(user = request.user).first(),
            count = cnt
        )
        tmp.save()
    
    context = {'username': str(request.user.username),
            "isPutCart": isPutCart}
    
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
def put_shopping_cart(request):
    # ajax 통신을 통해서 template에서 POST방식으로 전달
    onSaleProduct_id = request.POST.get('onSaleProduct_id', None)
    cnt = int(request.POST.get('cnt', 1))
    inDetail = request.POST.get('inDetail', False)

    shoppingCartList = ShoppingCart.objects.all()
    shoppingCartList = shoppingCartList.filter(customer__user=request.user)

    isPutCart = True

    for cartProduct in shoppingCartList:
        if int(cartProduct.onSaleProduct.id) == int(onSaleProduct_id):
            if inDetail:
                isPutCart = True
                tmp = cartProduct
                tmp.count += cnt
                tmp.save()
            else:
                isPutCart = False
                tmp = cartProduct
                tmp.delete()
            break
    else:
        isPutCart = True
        tmp = ShoppingCart(
            onSaleProduct = OnSaleProduct.objects.filter(pk = onSaleProduct_id).first(), 
            customer = Customer.objects.filter(user = request.user).first(),
            count = cnt
        )
        tmp.save()
    
    context = {'username': str(request.user.username),
            "isPutCart": isPutCart}
    
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
def shoppingcart_list(request):
    shops = Shop.objects.all()
    shoppings = ShoppingCart.objects.all()
    shoppings = shoppings.filter(customer__user=request.user)
    for shoppingProduct in shoppings:
        for shop in shops:
            if shoppingProduct.onSaleProduct.shop.company.name == shop.company.name and shoppingProduct.onSaleProduct.shop.name == shop.name:
                shop.isInCart = True
    return render(request,'shoppingcart.html',{'shoppings': shoppings, 'shops': shops})

    # on_sale_products = OnSaleProduct.objects.all()
    # on_sale_products = on_sale_products.filter(endDate__gt=time_threshold, stock__gt = 0) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
    # on_sale_products = on_sale_products[::-1] # 최근에 등록된 상품이 앞으로 오게 한다.