from django.shortcuts import render
import random 

# Create your views here.
def purchasecode(request):
    code = random.randrange(0, 9999)
    code = (4 - len(str(code))) * "0" + str(code)
    return render(request, 'customerPurchase/purchasecode.html', {'code':code})

def purchase_main(request):
    return render(request, "customerPurchase/purchase_main.html")

def Lpay(request):
    return render(request, "customerPurchase/Lpay.html")

def card(request):
    return render(request, "customerPurchase/card.html")

def phone(request):
    return render(request, "customerPurchase/phone.html")