from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from onSaleProduct.models import OnSaleProduct
from .models import ShoppingCart

@login_required
def like(request):
    # ajax 통신을 통해서 template에서 POST방식으로 전달
    onSaleProduct_id = request.POST.get('onSaleProduct_id', None)

    onSaleProduct = get_object_or_404(onSaleProduct, pk=onSaleProduct_id)

    if request.user in onSaleProduct.like.all():
        onSaleProduct.like.remove(request.user)
        isLiked = False
        message = "좋아요 취소"
    else:
        isLiked = True
        onSaleProduct.like.add(request.user)
        message = "좋아요"
    
    represent_user = ""
    if len(onSaleProduct.like.all()) > 0:
        represent_user = onSaleProduct.like.all()[0].username
    
    context = {'username': str(request.user.username),
            "isLiked": isLiked}
    
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
def shoppingcart_list(request):
    shoppings = ShoppingCart.objects.all()
    shoppings = shoppings.filter(customer__user=request.user)
    print(shoppings)
    return render(request,'shoppingcart.html',{'shoppings': shoppings})

    # on_sale_products = OnSaleProduct.objects.all()
    # on_sale_products = on_sale_products.filter(endDate__gt=time_threshold, stock__gt = 0) # 상품이 시장 철수를 하였거나, 할인이 마감된 할인 상품은 배제한다.
    # on_sale_products = on_sale_products[::-1] # 최근에 등록된 상품이 앞으로 오게 한다.