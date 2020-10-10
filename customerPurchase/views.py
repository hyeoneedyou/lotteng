from django.shortcuts import render
import random 

# Create your views here.
def purchasecode(request):
    code = random.randrange(0, 9999)
    code = (4 - len(str(code))) * "0" + str(code)
    return render(request, 'customerPurchase/purchasecode.html', {'code':code})