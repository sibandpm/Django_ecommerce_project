from datetime import datetime
from http.client import responses
import json
from django.http import JsonResponse
#from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponse
from mysite import models
from rest_framework import generics
from . import serializer
from . models import Invoices
# Create your views here.

#Home Page
def index(request):
    return render(request,'mysite/index.html')

#Products Page
def products(request):
    queryset = models.products.objects.all()
    return render(request, 'mysite/products.html', {'products': queryset})


#Cart Page
def ShoppingCart(request):
    return render(request,'mysite/cart.html')


#About Us 
def about(request):
    return render(request,'mysite/about.html')

#checkout
def checkout(request):
    return render(request,'mysite/checkout.html')

#checkout
def contact(request):
    return render(request,'mysite/contact.html')

#checkout
def login(request):
    return render(request,'mysite/login.html')

#order
def order(request):
    if request.method == 'POST':
        return render(request,'mysite/order.html')

    else:
       return index(request)


#checkout
def ordercomplete(request):
    if(request.method=='GET'):
        shopping_list = request.POST.get('shopping_list')
        billingemail = request.POST.get('billing-email')
        name = request.POST.get('billing-name')
        addr = request.POST.get('billing-addr')
        zip = request.POST.get('billing-zip')
        city = request.POST.get('billing-city')
        country = request.POST.get('billing-country')
        cost = request.POST.get('shipping-cost')
        card = request.POST.get('card_number')
        expdate = request.POST.get('expiration_date')
        cvc = request.POST.get('cvc')

        cartitems = json.loads(shopping_list)
        

        cus = models.Customers.objects.filter(email=billingemail).first()
        cusno=0
        totalprice=0
        noitems=0
        newinvoice=None
        customer=None
        if (cus is None):
            newcustomer= models.Customers(name=name,lastname=name,cellno=0,email=billingemail)
            models.Customers.save(newcustomer)
            cusno = newcustomer.customerno
            customer = newcustomer
        else:
            cusno = cus.customerno
            customer = cus
        
        newinvoice = models.Invoices(invoicesamt=0,invoicesqty=0,invoicesdate=datetime.today(),invoicestype=0,invoicesfor=customer)
        #newinvoice = Invoices.objects.create(invoicesamt=0, invoicesqty=0, invoicesdate=datetime.today(), invoicestype=0, invoicesfor=customer)
        models.Invoices.save(newinvoice)    
        

        newcart = models.Cart(cartqty=0,cartprice=0,invoice=newinvoice,cartstate=0,customerno=customer)

        models.Cart.save(newcart)

        for item in cartitems['items']:
            prod = models.Products.objects.get(idproducts=int(item['prodid']))
            newcartitem = models.Cartitems(cart=newcart,product=prod)
            totalprice +=item['price']
            noitems +=item['qty']
            models.Cartitems.save(newcartitem)

        newinvoice.invoicesamt=totalprice
        newinvoice.invoicesqty=noitems
        newinvoice.save()

        newcart.cartprice=totalprice
        newcart.cartqty=noitems
        newcart.save()
      
    return render(request,'mysite/completed.html')#,{'invoiceno': newinvoice.idinvoices})
    #return HttpResponse("Invalid request method.")

# def home(request):
#     customer=1000
#     param1 = {
#         'name': models.Customers.objects.get(customerno=customer)
#     }
#     if len(param1)<=0:
#         return render(request,'login.html')
#     else:
#         return render(request,'index.html',param1)
    


# def dashboard(request):
#     username = "Monty Phahlane"
#     return render(request,'home.html',{'loggedinname':username})

# def landing(request):
#     loggedinuser = {
#         'user': models.Customers.objects.get(customerno=1000)
#     }
#     return render(request,'dashboard.html',loggedinuser)

def customers(request):
     customer_list = models.Customers.objects.all() 
     return render(request, 'customers.html', {'customer_list': customer_list})

def customer(request, customerno):
     customer = models.Customers.objects.get(customerno=customerno) 
     cus =models.Customers(name='Me',lastname='You',cellno=customerno,email='me@you.com')
     models.Customers.save(cus)
     return render(request, 'customer.html', {'customer': customer})


# class CustomerListView(generics.ListCreateAPIView):
#     queryset = models.Customers.objects.all()
#     serializer_class = serializer.CustomersSerializer


    
# class ProductsListView(generics.ListCreateAPIView):
#     queryset = models.Products.objects.all()
#     serializer_class = serializer.ProductsSerializer

# class ProductView(generics.ListCreateAPIView):

#     serializer_class = serializer.ProductsSerializer
#     def get_queryset(self):
#         # Access the 'param' URL parameter using self.kwargs
#         param = self.kwargs.get('param')

#         # Filter the queryset based on the 'param' value
#         queryset = models.Products.objects.get(idproducts=param)

#         return queryset

    
# class CartView(generics.ListCreateAPIView):
#     queryset = models.Cart.objects.all()
#     serializer_class = serializer.CartSerializer