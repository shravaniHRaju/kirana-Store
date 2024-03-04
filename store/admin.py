from django.contrib import admin
#from store import models
from . import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.Unit)
admin.site.register(models.product)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id','product','qty','price','total_amt','vendor','pur_date']


admin.site.register(models.Purchase,PurchaseAdmin)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id','product','qty','price','total_amt']
admin.site.register(models.Sale,SaleAdmin)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product','pur_qty','sale_qty','total_bal_qty']
admin.site.register(models.Inventory,InventoryAdmin)
