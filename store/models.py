from django.db import models
from django.utils import timezone
date_field = models.DateField(default=timezone.now)

# Create your models here.
# vendor
class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "1. Vendors"

    def __str__(self):
        return self.full_name


# unit
class Unit(models.Model):
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "2. Unit"

    def __str__(self):
        return self.title


# product
class product(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "3. Product"

    def __str__(self):
        return self.title


# Purchase
class Purchase(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    total_amt = models.FloatField(editable=False, default=0)

    #pur_date=models.DateTimeField(auto_now=False)
    #check here pur_date
    pur_date = models.DateField(default=timezone.now)
    class Meta:
        verbose_name_plural = "4. Purchase"

    def save(self, *args, **kwargs):
        self.total_amt = self.qty * self.price
        super(Purchase, self).save(*args, **kwargs)

        # inventory effect
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty + self.qty
        else:
            totalBal = self.qty
        Inventory.objects.create(
            product=self.product,
            purchase=self,
            sale=None,
            pur_qty=self.qty,
            sale_qty=None,
            total_bal_qty=totalBal

        )


# Sale
class Sale(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    total_amt = models.FloatField(editable=False)
    sale_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=50, blank=True)
    customer_mobile = models.CharField(max_length=50)
    customer_address = models.TextField()

    class Meta:
        verbose_name_plural = "5. Sale"
    def save(self, *args, **kwargs):
        self.total_amt = self.qty * self.price
        super(Sale, self).save(*args, **kwargs)

        # sale effect
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty - self.qty
        """else:
            totalBal = self.qty"""
        Inventory.objects.create(
            product=self.product,
            purchase=None,
            sale=self,
            pur_qty=None,
            sale_qty=self.qty,
            total_bal_qty=totalBal

        )



# Inventory
class Inventory(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, default=0, null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, default=0, null=True)
    pur_qty = models.FloatField(default=0, null=True)
    sale_qty = models.FloatField(default=0, null=True)
    total_bal_qty = models.FloatField()

    class Meta:
        verbose_name_plural = "6. Inventory"
