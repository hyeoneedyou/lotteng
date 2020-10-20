from django.db import models

# 지도에 표시될 각 매장의 정보 모델
class ShopInfo(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=45)          #name = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shopName")
    latitude = models.CharField(max_length=45)      #latitude = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="lat")
    longitude = models.CharField(max_length=45)     #longitude = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="lng")
    company = models.CharField(max_length=45)       #company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")