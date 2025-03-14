from django.db import models


# CLIENTS TABLE IN DATABASE
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='إسم العميل')
    vehicle_plate = models.IntegerField(verbose_name='رقم لوحة السيارة')
    phone = models.CharField(max_length=15, verbose_name='رقم الجوال')
    washcount = models.IntegerField(default=0, verbose_name='عدد الغسلات')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "العملاء"