from django.db import models

# Create your models here.

class Address(models.Model):
    addressno = models.AutoField(primary_key=True)
    streetname = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    code = models.IntegerField(blank=True, null=True)
    addresstype = models.IntegerField(blank=True, null=True)
    addresslabel = models.CharField(max_length=50, blank=True, null=True)
    customerno = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerno')

    class Meta:
        managed = False
        db_table = 'address'



class cart(models.Model):
    idcart = models.AutoField(primary_key=True)
    cartqty = models.IntegerField(blank=True, null=True)
    cartprice = models.FloatField(blank=True, null=True)
    invoice = models.ForeignKey('Invoices', models.DO_NOTHING, db_column='invoice', blank=True, null=True)
    cartstate = models.IntegerField(blank=True, null=True)
    customerno = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'
        db_table_comment = '\t\t\t'



class Cards(models.Model):
    cardno = models.AutoField(primary_key=True)
    cardnumber = models.CharField(max_length=50)
    cardholder = models.CharField(max_length=100)
    expirydate = models.CharField(max_length=10)
    cvv = models.IntegerField()
    customerno = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerno', blank=True, null=True)
    addressno = models.ForeignKey(Address, models.DO_NOTHING, db_column='addressno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'


class Cartitems(models.Model):
    idcartitems = models.AutoField(primary_key=True)
    cart = models.ForeignKey(cart, models.DO_NOTHING, db_column='cart', blank=True, null=True)
    products = models.ForeignKey('products', models.DO_NOTHING, db_column='products', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartitems'


class Customers(models.Model):
    customerno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cellno = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customers'


class Delivery(models.Model):
    iddelivery = models.IntegerField(primary_key=True)
    deliverystatus = models.IntegerField(blank=True, null=True)
    deliverydate = models.DateTimeField(blank=True, null=True)
    shippingdate = models.DateTimeField(blank=True, null=True)
    scheduleddate = models.DateTimeField(blank=True, null=True)
    invoice = models.ForeignKey('Invoices', models.DO_NOTHING, db_column='invoice', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Invoices(models.Model):
    idinvoices = models.AutoField(primary_key=True)
    invoicesamt = models.FloatField(blank=True, null=True)
    invoicesqty = models.IntegerField(blank=True, null=True)
    invoicesdate = models.DateTimeField(blank=True, null=True)
    invoicestype = models.IntegerField(blank=True, null=True)
    invoicesfor = models.ForeignKey(Customers, models.DO_NOTHING, db_column='invoicesfor')
  
    class Meta:
        managed = False
        db_table = 'invoices'
        db_table_comment = '\t'


class productcategory(models.Model):
    idproductcategory = models.IntegerField(primary_key=True)
    productcategory = models.CharField(max_length=100, blank=True, null=True)
    productcategorydescr = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productcategory'


class products(models.Model):
    idproducts = models.IntegerField(primary_key=True)
    productscode = models.CharField(max_length=45, blank=True, null=True)
    productsname = models.CharField(max_length=200, blank=True, null=True)
    productsdescription = models.CharField(max_length=2000, blank=True, null=True)
    productsprice = models.FloatField(blank=True, null=True)
    productscat = models.ForeignKey(productcategory, models.DO_NOTHING, db_column='productscat')
    productsimg = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'