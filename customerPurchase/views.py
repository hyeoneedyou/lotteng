from django.shortcuts import render
import random 

# Create your views here.
def purchasecode(request):
    code = random.randrange(1000, 9999)
    return render(request, 'customerPurchase/purchasecode.html', {'code':code})