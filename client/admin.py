from django.contrib import admin
from .models import Client


# ADMIN PANEL CUSTOM
admin.site.site_header = "نظام مغاسل خمسة"
admin.site.site_title = "مغسلة سيارات"



# CLIENT APPEARNS IN ADMIN PANEL
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','vehicle_plate','phone','washcount')
    search_fields = ('name','vehicle_plate','washcount',)


admin.site.register(Client, ClientAdmin)